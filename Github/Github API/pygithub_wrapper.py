from github import Auth
from github import Github

# username of github
USERNAME = '40843245'
# password of github
PASSWORD = 'Github40843245'
# Github Token (beta)
GITHUB_TOKEN_BETA = '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'
# Github Token (classic)
GITHUB_TOKEN_CLASSIC = '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'

class PygithubWrapper():
	"""
		Description:
			constructor
		Parameter:
			None
		Returned Value:
			None
	"""
	def __init__(self):
		self.auth = None
		self.github = None
	"""
		Description:
			get the authentication access by GITHUB_TOKEN_CLASSIC.
		Parameter:
			None
		Returned Value:
			None
	"""
	def token(self):
		self.auth = Auth.Token(GITHUB_TOKEN_CLASSIC)
		self.github = Github(auth=self.auth)
	
	"""
		Description:
			format codescan alert `alert`.
		Parameter:
			alert: one elem of codescan alert.
		Returned Value:
			Returns a string after codescan alert is formatted.
	"""
	def format_codescan_alert(alert) -> str:
		s=''
		s+=alert.number
		s+=' '
		s+=alert.created_at
		s+=' '
		s+=alert.dismissed_at
		s+='\t'
		s+=alert.tool.name
		s+=' '
		s+=alert.tool.version
		s+=' '
		s+=alert.tool.guid
		s+='\t'
		s+=alert.rule.name
		s+=' ' 
		s+=alert.rule.security_severity_level
		s+=' '
		s+=alert.rule.severity
		s+='\t'
		s+=alert.rule.description
		s+=' '
		s+=alert.most_recent_instance.ref
		s+=' '
		s+=alert.most_recent_instance.state
		s+='\t'
		s+=alert.most_recent_instance.location
		s+='\t'
		s+=alert.most_recent_instance.message['text']

		return s

if __name__ == '__main__':
	my_PygithubWrapper = PygithubWrapper()
	my_PygithubWrapper.token()
	for repo in my_PygithubWrapper.github.get_user().get_repos():
		print(repo)
