#This code sends an email using Simple Email Service (SES) when the current local time arrives at a certain point. 

import boto3, json, json
region =  region  
EventBridge_Client = boto3.client('events', region_name = region)
current_time = datetime.datetime.now().time()
if current_time.hour == 0 and current_time.minute == 32:
    EventBridge_Client.put_rule(
        Name ='sample-event-rule',
        EventPattern ='{ "source": [ "SES-event" ], "detail-type": [ "SES-event-detail" ] }',
        State ='ENABLED',
        Description = 'Trigger a Lambda function to send an email when an eventbridge rule is triggered.'
        )

    EventBridge_Client.put_targets(Rule = 'sample-event-rule',
                                   Targets = [
                                       {
                                           'Id': 'LambdaSES',
                                           'Arn': 'Lambda function ARN (different from Lambda Execution Role ARN!)'
                                           },
                                           ]
                                           )
    
def send_email():
    # Initialize the SES client
    ses_client = boto3.client('ses', region_name=region)
    
    # Create an email template
    template_name = 'alarm-template'
    template_subject = 'subject'
    template_text = 'text'
    
    
    # Send the templated email
    response = ses_client.send_templated_email(
        Source='john.doe@gmail.com',
        Destination={
            'ToAddresses': ['jane.doe@gmail.com'],
            'CcAddresses': ['michael.doe@gmail.com']
        },
        ReplyToAddresses=['john.doe@gmail.com'],
        Template=template_name,
        TemplateData='{}'  # You can provide JSON data here to customize the template
    )
if __name__ == '__main__':
    send_email()
