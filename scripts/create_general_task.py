import argparse
import os
import asana
import datetime
from pathlib import Path
import datetime

import warnings
warnings.filterwarnings("ignore")

# @icaoberg Read secrets. Assumes file exists in ~/.ASANA_SECRETS
file = str(Path.home()) + os.sep + '.ASANA_SECRETS'
exec(open(file).read())

client = asana.Client.access_token(PERSONAL_ACCESS_TOKEN)

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--message", dest="message", default=None)
parser.add_argument("-n", "--notes", dest="notes", default=None)
parser.add_argument("-d", "--delta", dest="delta", default=14)

args = parser.parse_args()

delta = int(args.delta)

if args.notes is None:
	notes = None
else:
	notes = args.notes

if args.message is None:
	message = None
else:
	message = args.message

if args.notes is None:
	notes = None
else:
	notes = args.notes

username='1183587634011025' #icaoberg
workspace='1132331877475002' #PSC

when=datetime.date.today() + datetime.timedelta(days=delta+1)

if message is None or message == '':
	print('Cannot create task with an empty message.')
else:
	params={'name': message, \
        	'assignee': username, \
        	'due_on': str(when+datetime.timedelta(days=delta+1+delta)), \
		'assignee_status': 'later', \
        	'start_on': str(when)}

	if notes is not None and notes != '':
		params['notes'] = notes

	answer = client.tasks.create_in_workspace(workspace,params)
