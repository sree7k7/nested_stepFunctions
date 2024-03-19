from aws_cdk import (
    # Duration,
    Stack,
    RemovalPolicy,
    # aws_sqs as sqs,
    aws_iam as iam,
    aws_lambda as _lambda
)
from constructs import Construct
import aws_cdk.aws_stepfunctions as sfn
import aws_cdk.aws_logs as _logs
from aws_cdk import aws_stepfunctions_tasks as tasks

class NestedStepFunctionsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # # create a lambda function for to validate aws account id
        validate_account_id_lambda = _lambda.Function(
            self, "ValidateAccountIdLambda",
            runtime=_lambda.Runtime.PYTHON_3_12,
            log_group=_logs.LogGroup(
                self, "ValidateAccountId",
                log_group_name="/aws/lambda/validate_account",
                removal_policy=RemovalPolicy.DESTROY,
                retention=_logs.RetentionDays.ONE_DAY
            ),
            handler="validate_account_id.lambda_handler",
            code=_lambda.Code.from_asset("lambda")
        )

        # # create a lambda function for success
        success_lambda = _lambda.Function(
            self, "SuccessLambda",
            runtime=_lambda.Runtime.PYTHON_3_12,
            log_group=_logs.LogGroup(
                self, "SuccessLambdaGroup",
                log_group_name="/aws/lambda/success",
                removal_policy=RemovalPolicy.DESTROY,
                retention=_logs.RetentionDays.ONE_DAY
            ),
            handler="success_lambda.lambda_handler",
            code=_lambda.Code.from_asset("lambda")
        )

        # # create a lambda function for failure
        failure_lambda = _lambda.Function(
            self, "FailureLambda",
            runtime=_lambda.Runtime.PYTHON_3_12,
            log_group=_logs.LogGroup(
                self, "FailureLambdaGroup",
                log_group_name="/aws/lambda/failure",
                removal_policy=RemovalPolicy.DESTROY,
                retention=_logs.RetentionDays.ONE_DAY
            ),
            handler="failure_lambda.lambda_handler",
            code=_lambda.Code.from_asset("lambda")
        )   
        # Define an IAM role with necessary permissions
        role = iam.Role(self, "Role", assumed_by=iam.ServicePrincipal("states.amazonaws.com"))
        role.add_to_policy(iam.PolicyStatement(
            actions=["states:StartExecution"],
            # resources=[another_state_machine.state_machine_arn]
            resources=["*"]
        ))

        # Define the state machine definition
        # definition = tasks.LambdaInvoke(self, 
        #     "Invoke Lambda - Validate account number",
        #     lambda_function=check_account_number_lambda,
        #     output_path="$.Payload",
        # ).add_retry(max_attempts=3).next(
        #     sfn.Choice(self, "is Account number 12 bytes")
        #     .when(sfn.Condition.number_equals("$.statusCode", 200),
        #         tasks.LambdaInvoke(self, "Invoke Lambda - HelloLambda",
        #             lambda_function=hello_world_lambda,
        #             output_path="$.Payload",
        #         ).add_retry(max_attempts=3).next(
        #             sfn.Succeed(self, "Success")
        #         )
        #     )
        #     .when(sfn.Condition.number_equals("$.statusCode", 400),
        #         sfn.Fail(self, "Fail")
        #     )
        # )

        state_machine_name = sfn.StateMachine(
            self,
            "statemachine",
            state_machine_name="statemach"
        )

        definition = tasks.StepFunctionsStartExecution(
            self,
            "StartExecution",
            state_machine=state_machine_name,
            definition="YOUR_DEFINITION_HERE"
        )

        # create a state machine
        # another_state_machine = sfn.StateMachine.
        # definition = sfn.Pass(self, "StartState")
        
        
        # simple_state_machine = sfn.StateMachine(self, "SimpleStateMachine",
        #     definition=definition,
        #     state_machine_name="SimpleStateMachine",
        #     role=role,
        # )

        

        # Create a StepFunctionsStartExecution task
        # start_execution_task = sfn_tasks.StepFunctionsStartExecution(
        #     self, "StartExecution",
        #     state_machine=simple_state_machine,
        #     name="StartExecution",
        #     input=sfn.TaskInput.from_object({
        #         "executionInput.$": "$"
        #     })  # Pass the state input as the execution input
        # )

        # # Create Choice state
        # choice_state = sfn.Choice(self, "ChoiceState")

        # # Add conditions to the Choice state
        # choice_state.when(sfn.Condition.string_equals("$.choice", "option1"), sfn.Pass(self, "Option1"))
        # choice_state.when(sfn.Condition.string_equals("$.choice", "option2"), sfn.Pass(self, "Option2"))
        # choice_state.otherwise(sfn.Fail(self, "FailState", error="Unknown choice"))

        # Connect the StartExecution task to the Choice state
        # start_execution_task.next(choice_state)

        # Create a state machine with the StartExecution task as the definition
        # step_function = sfn.StateMachine(
        #     self, "StepFunction",
        #     definition=start_execution_task
        # )