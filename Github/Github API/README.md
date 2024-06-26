# pygithub_wrapper.py
## Intro
A wrapper class of PyGithub module.

## Prequisite
1. Install modules (at Dependency section)
2. Follow steps on Quickstart guide section.

## Dependency
1. PyGithub

## Dependency Docs
1. PyGithub

https://pygithub.readthedocs.io/en/stable/introduction.html

## Quickstart guide
### Part 1
To access data about GitHub, one must follow one of these:
1. Login.
2. Authenticate with token.

#### How to generateb a(n) Token in Github?
See

https://www.geeksforgeeks.org/how-to-generate-personal-access-token-in-github/#:~:text=1%20Step%201%3A%20Click%20on%20the%20profile%20image,8%3A%20Your%20Personal%20access%20token%20is%20created%20successfully
#### Login in PyGithub
Login Github with username and password.

In PyGithub, it can be achieve with piece of code.

    # username of github
    USERNAME = <your_username>
    # password of github
    PASSWORD = <your_password>

    auth = github.Auth.Login(USERNAME,PASSWORD)
    github.Github(auth=auth)

#### Authenticate with token in PyGithub
In Github, there are two different kind of Personal access tokens.
1. Fine-granted tokens (beta).
2. Tokens (classic).

Since Fine-granted tokens (beta) is experimental, I highly recommend that use Tokens (classic) NOT Fine-granted tokens (beta).

Generate a(n) Tokens (classic) then copy the token, replace the <your_classic_token> of line with the token.

    GITHUB_TOKEN_CLASSIC = <your_classic_token>

In PyGithub, it can be achieve with piece of code to authenticate the account.

    # Github Token (classic)
    GITHUB_TOKEN_CLASSIC = <your_classic_token>

    auth = github.Auth.Login(USERNAME,PASSWORD)
    github.Github(auth=auth)

I wrapped the above code as:
    
    # Github Token (classic)
    GITHUB_TOKEN_CLASSIC = <your_classic_token>
    
    my_PygithubWrapper = PygithubWrapper()
	my_PygithubWrapper.token()

## API
### token
    def token(self)
### format_codescan_alert
    def format_codescan_alert(alert) -> str
## Source Code
Available at pygithub_wrapper.py.

## More details
For more details about API, see comments of source code at pygithub_wrapper.py.
