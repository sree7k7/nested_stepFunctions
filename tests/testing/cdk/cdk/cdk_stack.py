from aws_cdk import Stack
import aws_cdk as cdk
import aws_cdk.aws_iam as iam
import aws_cdk.aws_stepfunctions as stepfunctions
from constructs import Construct

class CdkStack(Stack):
  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    # Resources
    iamManagedPolicy00policyserviceroleLambdaInvokeScopedAccessPolicyaebc92d155474dc6906a14eb0629919c00b7EMw = iam.CfnManagedPolicy(self, 'IAMManagedPolicy00policyserviceroleLambdaInvokeScopedAccessPolicyaebc92d155474dc6906a14eb0629919c00b7EMw',
          managed_policy_name = 'LambdaInvokeScopedAccessPolicy-aebc92d1-5547-4dc6-906a-14eb0629919c',
          path = '/service-role/',
          description = 'Allow AWS Step Functions to invoke Lambda functions on your behalf',
          groups = [
          ],
          policy_document = {
            'Version': '2012-10-17',
            'Statement': [
              {
                'Resource': [
                  'arn:aws:lambda:eu-central-1:619831221558:function:helloworld:*',
                  'arn:aws:lambda:eu-central-1:619831221558:function:FailedHelloFunction:*',
                ],
                'Action': [
                  'lambda:InvokeFunction',
                ],
                'Effect': 'Allow',
              },
              {
                'Resource': [
                  'arn:aws:lambda:eu-central-1:619831221558:function:helloworld',
                  'arn:aws:lambda:eu-central-1:619831221558:function:FailedHelloFunction',
                ],
                'Action': [
                  'lambda:InvokeFunction',
                ],
                'Effect': 'Allow',
              },
            ],
          },
          roles = [
            'StepFunctions-MyStateMachine-her39as55-role-dh2wet5w2',
          ],
          users = [
          ],
        )
    iamManagedPolicy00policyserviceroleLambdaInvokeScopedAccessPolicyaebc92d155474dc6906a14eb0629919c00b7EMw.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.RETAIN

    iamManagedPolicy00policyserviceroleStepFunctionsStartExecutionManagementScopedAccessPolicy8b2d3abf294f4d8c9883d2302dfc384f00g3bKv = iam.CfnManagedPolicy(self, 'IAMManagedPolicy00policyserviceroleStepFunctionsStartExecutionManagementScopedAccessPolicy8b2d3abf294f4d8c9883d2302dfc384f00g3bKv',
          managed_policy_name = 'StepFunctionsStartExecutionManagementScopedAccessPolicy-8b2d3abf-294f-4d8c-9883-d2302dfc384f',
          path = '/service-role/',
          description = 'Allows AWS Step Functions to start another workflow execution on your behalf.',
          groups = [
          ],
          policy_document = {
            'Version': '2012-10-17',
            'Statement': [
              {
                'Resource': [
                  'arn:aws:states:eu-central-1:619831221558:stateMachine:STATE_MACHINE_NAME',
                ],
                'Action': [
                  'states:StartExecution',
                ],
                'Effect': 'Allow',
              },
              {
                'Resource': '*',
                'Action': [
                  'states:DescribeExecution',
                  'states:StopExecution',
                ],
                'Effect': 'Allow',
              },
              {
                'Resource': [
                  'arn:aws:events:eu-central-1:619831221558:rule/StepFunctionsGetEventsForStepFunctionsExecutionRule',
                ],
                'Action': [
                  'events:PutTargets',
                  'events:PutRule',
                  'events:DescribeRule',
                ],
                'Effect': 'Allow',
              },
            ],
          },
          roles = [
            'StepFunctions-MyStateMachine-her39as55-role-dh2wet5w2',
          ],
          users = [
          ],
        )
    iamManagedPolicy00policyserviceroleStepFunctionsStartExecutionManagementScopedAccessPolicy8b2d3abf294f4d8c9883d2302dfc384f00g3bKv.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.RETAIN

    iamManagedPolicy00policyserviceroleXRayAccessPolicy2397a1356cc44528ac46a135d277b15900Hr49A = iam.CfnManagedPolicy(self, 'IAMManagedPolicy00policyserviceroleXRayAccessPolicy2397a1356cc44528ac46a135d277b15900Hr49A',
          managed_policy_name = 'XRayAccessPolicy-2397a135-6cc4-4528-ac46-a135d277b159',
          path = '/service-role/',
          description = 'Allow AWS Step Functions to call X-Ray daemon on your behalf',
          groups = [
          ],
          policy_document = {
            'Version': '2012-10-17',
            'Statement': [
              {
                'Resource': [
                  '*',
                ],
                'Action': [
                  'xray:PutTraceSegments',
                  'xray:PutTelemetryRecords',
                  'xray:GetSamplingRules',
                  'xray:GetSamplingTargets',
                ],
                'Effect': 'Allow',
              },
            ],
          },
          roles = [
            'StepFunctions-MyStateMachine-her39as55-role-dh2wet5w2',
          ],
          users = [
          ],
        )
    iamManagedPolicy00policyserviceroleXRayAccessPolicy2397a1356cc44528ac46a135d277b15900Hr49A.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.RETAIN

    iamRole00StepFunctionsMyStateMachineher39as55roledh2wet5w2009H7rz = iam.CfnRole(self, 'IAMRole00StepFunctionsMyStateMachineher39as55roledh2wet5w2009H7rz',
          path = '/service-role/',
          managed_policy_arns = [
            iamManagedPolicy00policyserviceroleXRayAccessPolicy2397a1356cc44528ac46a135d277b15900Hr49A.ref,
            iamManagedPolicy00policyserviceroleLambdaInvokeScopedAccessPolicyaebc92d155474dc6906a14eb0629919c00b7EMw.ref,
            iamManagedPolicy00policyserviceroleStepFunctionsStartExecutionManagementScopedAccessPolicy8b2d3abf294f4d8c9883d2302dfc384f00g3bKv.ref,
            'arn:aws:iam::aws:policy/AdministratorAccess',
          ],
          max_session_duration = 3600,
          role_name = 'StepFunctions-MyStateMachine-her39as55-role-dh2wet5w2',
          assume_role_policy_document = {
            'Version': '2012-10-17',
            'Statement': [
              {
                'Action': 'sts:AssumeRole',
                'Effect': 'Allow',
                'Principal': {
                  'Service': 'states.amazonaws.com',
                },
              },
            ],
          },
        )
    iamRole00StepFunctionsMyStateMachineher39as55roledh2wet5w2009H7rz.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.RETAIN

    stepFunctionsStateMachine00stateMachineMyStateMachineher39as5500H5wyA = stepfunctions.CfnStateMachine(self, 'StepFunctionsStateMachine00stateMachineMyStateMachineher39as5500H5wyA',
          definition_string = '{\"Comment\":\"A description of my state machine\",\"StartAt\":\"Step Functions StartExecution\",\"States\":{\"Step Functions StartExecution\":{\"Type\":\"Task\",\"Resource\":\"arn:aws:states:::states:startExecution.sync:2\",\"Parameters\":{\"StateMachineArn\":\"arn:aws:states:eu-central-1:619831221558:stateMachine:AccountValidation\",\"Input\":{\"accountId\":\"619831221558\"}},\"Next\":\"Choice\"},\"Choice\":{\"Type\":\"Choice\",\"Choices\":[{\"Variable\":\"$.Output.statusCode\",\"NumericEquals\":200,\"Next\":\"Lambda Invoke\"},{\"Variable\":\"$.Output.statusCode\",\"NumericEquals\":400,\"Next\":\"LambdaWorkingForFailed\"}]},\"Lambda Invoke\":{\"Type\":\"Task\",\"Resource\":\"arn:aws:states:::lambda:invoke\",\"OutputPath\":\"$.Payload\",\"Parameters\":{\"Payload.$\":\"$\",\"FunctionName\":\"arn:aws:lambda:eu-central-1:619831221558:function:choiceHelloWorld:$LATEST\"},\"Retry\":[{\"ErrorEquals\":[\"Lambda.ServiceException\",\"Lambda.AWSLambdaException\",\"Lambda.SdkClientException\",\"Lambda.TooManyRequestsException\"],\"IntervalSeconds\":1,\"MaxAttempts\":3,\"BackoffRate\":2}],\"End\":true},\"LambdaWorkingForFailed\":{\"Type\":\"Task\",\"Resource\":\"arn:aws:states:::lambda:invoke\",\"OutputPath\":\"$.Payload\",\"Parameters\":{\"Payload.$\":\"$\",\"FunctionName\":\"arn:aws:lambda:eu-central-1:619831221558:function:FailedHelloFunction:$LATEST\"},\"Retry\":[{\"ErrorEquals\":[\"Lambda.ServiceException\",\"Lambda.AWSLambdaException\",\"Lambda.SdkClientException\",\"Lambda.TooManyRequestsException\"],\"IntervalSeconds\":1,\"MaxAttempts\":3,\"BackoffRate\":2}],\"End\":true}}}',
          logging_configuration = {
            'includeExecutionData': False,
            'level': 'OFF',
          },
          state_machine_name = 'MyStateMachine-her39as55',
          role_arn = iamRole00StepFunctionsMyStateMachineher39as55roledh2wet5w2009H7rz.attr_arn,
          tags = [
          ],
          state_machine_type = 'STANDARD',
          tracing_configuration = {
            'enabled': False,
          },
        )
    stepFunctionsStateMachine00stateMachineMyStateMachineher39as5500H5wyA.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.RETAIN