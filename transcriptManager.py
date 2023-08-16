"""
Authors: Yuneydy Paredes
Consulted:
Date: 2023-4-20
Purpose: transcript manager
"""

def onlyEvents(inputFile, outputFile):
    '''
    Writes the events to the output file in the same order they appear
    in the input file.
    '''
    with open(inputFile, 'r') as f:
        lines = f.readlines()
    events = [line for line in lines if ':' not in line]
    with open(outputFile, 'w') as f:
        f.writelines(events)

def listSenders(inputFile, outputFile):
    '''
    Writes the senders to the output file in the same order they appear
    in the input file.
    '''
    with open(inputFile, 'r') as f:
        lines = f.readlines()
    messages = [line for line in lines if ':' in line]
    senders = []
    for message in messages:
        sender = message.split(':')[0].strip()
        if sender in senders:
            senders = senders
        else:
            senders.append(sender)
    with open(outputFile, 'w') as f:
        f.write('\n'.join(senders))

def messagesWithWord(input_file, string, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
    messages = []
    for i in range(len(lines)):
        if ':' in lines[i]:
            message = lines[i+1].strip()
            if string.lower() in message.lower():
                messages.append(lines[i].strip() + '\n' + message + '\n')
    with open(output_file, 'w') as f:
        f.writelines(messages)
