from github import Github

class GitHubOperation():

    github = Github("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")
    availableFiles=[]
    @staticmethod
    def nothingFunc(*argvs):
        pass
    
    def __init__(self):
        self.PAT=None
        self.github=None
    
    def SetPAT(self,PAT:str):
        self.PAT=PAT

    def ConnectGitHub(self):
        self.github=Github(self.PAT)

    def GetGitHub(self):
        return self.github
    
    class Repo():

        @staticmethod
        def FindRepo(github
                 ,repoName:str
                 ):
            repos=github.get_user().get_repos()
            for repo in repos:
                if repoName == repo.name:
                    return repo
            return None
        
        @staticmethod
        def FindFileInRepo(github
                       ,fileName:str
                       ,repoName:str
                       ,func_whenIsDir=None
                       ,func_whenIsNotDir=None
                       ):
            if func_whenIsDir is None:
                func_whenIsDir = GitHubOperation.nothingFunc
            if func_whenIsNotDir is None:
                func_whenIsNotDir = GitHubOperation.nothingFunc
 
            result = None
            repo=GitHubOperation.Repo.FindRepo(github=github,repoName=repoName)
            if repo is None:
                raise ValueError("ERROR!!! The repo is NOT found!!!")
            contents = repo.get_contents("")
            while contents:
                file_content = contents.pop(0)
                if fileName == file_content.name:
                    result = file_content
                if file_content.type == "dir":
                    t=repo.get_contents(file_content.path)
                    contents.extend(t)
                    func_whenIsDir((t))
                else:
                    func_whenIsNotDir((file_content))
            return (result,GitHubOperation.allavailableFiles)

        def CreateRepo(github
                   ,repoName:str
                   ):
            repo=GitHubOperation.Repo.FindRepo(github=github,repoName=repoName)
            if not repo is None:
                raise ValueError("ERROR!!! The repo already exists!!!")
            github.get_user().create_repo(repoName)
     
        def CreateFileInRepo(github
                   ,fileName:str
                   ,repoName:str
                   ,message:str
                   ,content:str
                   ):
            repo=GitHubOperation.Repo.FindRepo(github=github,repoName=repoName)
            if repo is None:                    
                raise  ValueError("ERROR!!! The repo already exists!!!")
        
            (file_content,_)=self.FindFileInRepo(fileName=fileName,repoName=repoName)
            if not file_content is None:
                raise ValueError("ERROR!!! The file already exists!!!")
            repo.create_file(fileName,message=message,content=content)

        def DeleteFileInRepo(github
                   ,fileName:str
                   ,repoName:str
                   ,branch:str
                   ):
            repo=GitHubOperation.Repo.FindRepo(github=github,repoName=repoName)
            if repo is None:                    
                raise ValueError("ERROR!!! The repo does NOT exist!!!")
        
            (file_content,_)=GitHubOperation.Repo.FindFileInRepo(github=github,fileName=fileName,repoName=repoName)
            if file_content is None:
                raise ValueError("ERROR!!! The file does NOT exist!!!")
            tarBranch=GitHubOperation.Repo.FindBranchInRepo(github=github,repoName=repoName,branch=branch)
            if tarBranch is None:
                raise ValueError("ERROR!!! The branch does NOT exist!!!")
            repo.delete_file(file_content.path,"remove test",file_content.sha,branch=branch)
            print("Delete successfully.")

        def UpdateFileInRepo(github
                   ,fileName:str
                   ,repoName:str
                   ,content:str
                   ,message:str
                   ,branch:str
                   ):
            repo=GitHubOperation.Repo.FindRepo(github=github,repoName=repoName)
            if repo is None:                    
                raise ValueError("ERROR!!! The repo does NOT exist!!!")
            (file_content,_)=GitHubOperation.Repo.FindFileInRepo(github=github,fileName=fileName,repoName=repoName)
            if file_content is None:
                raise ValueError("ERROR!!! The file does NOT exist!!!")
            tarBranch=GitHubOperation.Repo.FindBranchInRepo(github=github,repoName=repoName,branch=branch)
            if tarBranch is None:
                raise ValueError("ERROR!!! The branch does NOT exist!!!")
            repo.update_file(file_content.path,content=content,message=message,sha=file_content.sha,branch=branch)
            print("Update the file successfully.")

        def GetAllAvailableFiles_Recursively(github
                                         ,repoName:str
                                         ):
            def func_whenIsDir(*argvs):
                pass
            def func_whenIsNotDir(v):
                GitHubOperation.allavailableFiles.append(v)
        
            GitHubOperation.allavailableFiles=[]
            (_,allAvailableFiles)=GitHubOperation.Repo.FindFileInRepo(github=github,fileName=""
                            ,repoName=repoName
                            ,func_whenIsDir=func_whenIsDir
                            ,func_whenIsNotDir=func_whenIsNotDir
                            )
            return GitHubOperation.allAvailableFiles

        def GetAllAvailableFoldersAndFiles_Recursively(github
                                         ,repoName:str
                                         ):
    
            def func_whenIsDir(v):
                GitHubOperation.allavailableFiles.append(v)
            def func_whenIsNotDir(*argvs):
                pass
        
            GitHubOperation.allavailableFiles=[]
            (_,allAvailableFiles)=GitHubOperation.Repo.FindFileInRepo(github=github,fileName=""
                            ,repoName=repoName
                            ,func_whenIsDir=func_whenIsDir
                            ,func_whenIsNotDir=func_whenIsNotDir
                            )
            return allAvailableFiles
    
        def GetScanningAlertInRepo(github
                                 ,repoName:str
                                ):
            repo=GitHubOperation.Repo.FindRepo(github=github,repoName=repoName)
            if repo is None:                    
                raise ValueError("ERROR!!! The repo does NOT exist!!!")
    
            codescan_alerts = repo.get_codescan_alerts()
            return codescan_alerts
            """
         for alert in codescan_alerts:
            print(alert.number, alert.created_at, alert.dismissed_at,sep="\t",end="\n")
            print("  ", alert.tool.name, alert.tool.version, alert.tool.guid,sep="\t",end="\n")
            print(alert.rule.name,alert.rule.security_severity_level,alert.rule.severity,sep="\t",end="\n")
            print("\t", alert.rule.description,sep="\t",end="\n")
            print("\t", alert.most_recent_instance.ref, alert.most_recent_instance.state,sep="\t",end="\n")
            print("\t", alert.most_recent_instance.location,sep="\t",end="\n")
            print("\t", alert.most_recent_instance.message['text'],sep="\t",end="\n")
            """
        @staticmethod
        def GetAllLabelsInRepo(github
                             ,repoName:str
                             ):
            repo=GitHubOperation.Repo.FindRepo(github=github,repoName=repoName)
            if repo is None:                    
                raise ValueError("ERROR!!! The repo does NOT exist!!!")
            labels = repo.get_labels()
            return labels
    
        @staticmethod
        def GetNumberOfViewsBreakdownFromLastDays(github
                                              ,repoName:str
                                              ,days:int
                                              ):
        
            if not isinstance(days,(int)):
                raise TypeError("ERROR!!! The parameter days must be an integer!!!")
            if days<=0 and days % 7 != 0 :
                raise ValueError("ERROR!!! The parameter days must be = n \n where n must be positive integer and multiple of 7.\n But here, n obeys the limitation.")
        
            repo=GitHubOperation.Repo.FindRepo(github=github,repoName=repoName)
            if repo is None:                    
                raise ValueError("ERROR!!! The repo does NOT exist!!!")
        
            weeks=int(days/7)
            contents = repo.get_views_traffic()
            for idx in range(1,weeks,1):
                contents = repo.get_views_traffic(per="week")
            return contents
        
        @staticmethod
        def GetNumberOfClonesBreakdownFromLastDays(github
                                ,repoName:str
                                ,days:int
                                ):
            if not isinstance(days,(int)):
                raise TypeError("ERROR!!! The parameter days must be an integer!!!")
            if days<=0 and days % 7 != 0 :
                raise ValueError("ERROR!!! The parameter days must be = n \n where n must be positive integer and multiple of 7.\n But here, n obeys the limitation.")
        
            repo=GitHubOperation.Repo.FindRepo(github=github,repoName=repoName)
            if repo is None:                    
                raise ValueError("ERROR!!! The repo does NOT exist!!!")
        
            weeks=int(days/7)
            contents = repo.get_clones_traffic()
            for idx in range(1,weeks,1):
                contents = repo.get_clones_traffic(per="week")
            return contents
    
        @staticmethod
        def GetTop10PopularContentsFromLastDays(github
                                ,repoName:str
                                ,days:int
                                ):
        
            if not isinstance(days,(int)):
                raise TypeError("ERROR!!! The parameter days must be an integer!!!")
            if days<=0 and days % 7 != 0 :
                raise ValueError("ERROR!!! The parameter days must be = n \n where n must be positive integer and multiple of 7.\n But here, n obeys the limitation.")        
            repo=GitHubOperation.Repo.FindRepo(github=github,repoName=repoName)
            if repo is None:                    
                raise ValueError("ERROR!!! The repo does NOT exist!!!")
            weeks=int(days/7)
            contents = repo.get_top_paths()
            return contents

        @staticmethod
        def GetTop10PopularReferrersFromLastDays(github
                                ,repoName:str
                                ,days:int
                                ):
        
            if not isinstance(days,(int)):
                raise TypeError("ERROR!!! The parameter days must be an integer!!!")
            if days<=0 and days % 7 != 0 :
                raise ValueError("ERROR!!! The parameter days must be = n \n where n must be positive integer and multiple of 7.\n But here, n obeys the limitation.")
        
            repo=GitHubOperation.Repo.FindRepo(github=github,repoName=repoName)
            if repo is None:                    
                raise ValueError("ERROR!!! The repo does NOT exist!!!")
        
            weeks=int(days/7)
            contents = repo.get_top_referrers()
            return contents

        @staticmethod
        def GetCountOfStars(github
                        ,repoName:str
                        ):
            repo=GitHubOperation.Repo.FindRepo(github=github,repoName=repoName)
            if repo is None:                    
                raise ValueError("ERROR!!! The repo does NOT exist!!!")
            return repo.stargazers_count
        
        @staticmethod
        def GetRepositoryTopics(github
                        ,repoName:str
                        ):
            repo=GitHubOperation.Repo.FindRepo(github=github,repoName=repoName)
            if repo is None:                    
                raise ValueError("ERROR!!! The repo does NOT exist!!!")
            return repo.get_topics()
        
    class Branch():
        @staticmethod
        def FindBranchInRepo(github
                         ,repoName:str
                         ,branch:str):
            repo=GitHubOperation.Repo.FindRepo(github=github,repoName=repoName)
            if repo is None:                    
                raise ValueError("ERROR!!! The repo does NOT exist!!!")
        
            branches=list(repo.get_branches())
            for v in branches:
                if branch == v.name:
                    return v
            return None
    
        @staticmethod
        def GetBranchIsProtected(github
                            ,repoName:str
                            ,branch:str
                            ):
            repo=GitHubOperation.Repo.FindRepo(github=github,repoName=repoName)
            if repo is None:                    
                raise ValueError("ERROR!!! The repo does NOT exist!!!")
        
            tarBranch=GitHubOperation.Repo.FindBranchInRepo(repoName=repoName,branch=branch)
            if tarBranch is None:
                raise ValueError("ERROR!!! The branch does NOT exist!!!")
            return tarBranch.protected
        
        @staticmethod
        def GetRequiredStatusChecksOfABranch(github
                                ,repoName:str
                                ,branch:str
                                ):
            repo=GitHubOperation.Repo.FindRepo(github=github,repoName=repoName)
            if repo is None:                    
                raise ValueError("ERROR!!! The repo does NOT exist!!!")
        
            tarBranch=GitHubOperation.Repo.FindBranchInRepo(github=github,repoName=repoName,branch=branch)
            if tarBranch is None:
                raise ValueError("ERROR!!! The branch does NOT exist!!!")
            return tarBranch.get_required_status_checks()

        @staticmethod
        def GetHeadCommitOfABranch(github
                                ,repoName:str
                                ,branch:str
                                ):
            repo=GitHubOperation.Repo.FindRepo(github=github,repoName=repoName)
            if repo is None:                    
                raise ValueError("ERROR!!! The repo does NOT exist!!!")
        
            tarBranch=GitHubOperation.Repo.FindBranchInRepo(github=github,repoName=repoName,branch=branch)
            if tarBranch is None:
                raise ValueError("ERROR!!! The branch does NOT exist!!!")
            return tarBranch.commit
        
    class Commit():
        @staticmethod
        def CreateCommitStatusCheck(github
                                ,repoName:str
                                ,state:str
                                ,target_url:str
                                ,description:str
                                ,context:str
                                ,sha
                                ):
            repo=GitHubOperation.Repo.FindRepo(github=github,repoName=repoName)
            if repo is None:                    
                raise ValueError("ERROR!!! The repo does NOT exist!!!")

            repo.get_commit(sha=sha).create_status(
                state=state,
                target_url=target_url,
                description=description,
                context=context
                )
            
        @staticmethod
        def GetCommit(github
                      ,repoName:str
                      ,sha
                      ):
            repo=GitHubOperation.Repo.FindRepo(github=github,repoName=repoName)
            if repo is None:                    
                raise ValueError("ERROR!!! The repo does NOT exist!!!")
            commit=repo.get_commit(sha=sha)
            return commit
        
    class PullRequest():
        @staticmethod
        def CreatePullRequest(github
                              ,repoName:str
                              ,title:str
                              ,body:str
                              ,head:str
                              ,base:str
                              ):
            repo=GitHubOperation.Repo.FindRepo(github=github,repoName=repoName)
            if repo is None:                    
                raise ValueError("ERROR!!! The repo does NOT exist!!!")
            
            repo.create_pull(title=title,body=body,head=head,base=base)
        
        @staticmethod
        def GetPullRequestbyNumber(github
                                   ,repoName:str
                                   ,number:int
                                   ):
            repo=GitHubOperation.Repo.FindRepo(github=github,repoName=repoName)
            if repo is None:                    
                raise ValueError("ERROR!!! The repo does NOT exist!!!")
            return repo.get_pull(number)
        @staticmethod
        def GetPullRequestsbyQuery(github
                                   ,repoName:str
                                   ,state:str
                                   ,sort:str
                                   ,base:str
                                   ):
            repo=GitHubOperation.Repo.FindRepo(github=github,repoName=repoName)
            if repo is None:                    
                raise ValueError("ERROR!!! The repo does NOT exist!!!")
            pulls = repo.get_pulls(state=state, sort=sort, base=base)
            return pulls
    
    class Issues():
        @staticmethod
        def GetIssue(github
                     ,repoName:str
                     ,number:int
                     ):
            repo=GitHubOperation.Repo.FindRepo(github=github,repoName=repoName)
            if repo is None:   
                raise ValueError("ERROR!!! The repo does NOT exist!!!")
            return repo.get_issue(number=number)
        
        @staticmethod
        def CreateCommentOnIssue(github
                     ,repoName:str
                     ,number:int
                     ,comments:str
                     ):
            issue=GitHubOperation.Issues.GetIssue(github=github,repoName=repoName,number=number)
            return issue.create_comment(comments)
        
        @staticmethod 
        def CreateIssue(github
                     ,repoName:str
                     ,title:str
                     ):
            repo=GitHubOperation.Repo.FindRepo(github=github,repoName=repoName)
            if repo is None:   
                raise ValueError("ERROR!!! The repo does NOT exist!!!")
            return repo.create_issue(title=title)
        
        @staticmethod 
        def CreateIssueWithBody(github
                     ,repoName:str
                     ,title:str
                     ,body:str
                     ):
            repo=GitHubOperation.Repo.FindRepo(github=github,repoName=repoName)
            if repo is None:   
                raise ValueError("ERROR!!! The repo does NOT exist!!!")
            return repo.create_issue(title=title,body=body)
        
        @staticmethod 
        def CreateIssueWithLabels(github
                     ,repoName:str
                     ,title:str
                     ,labelName:str
                     ):
            repo=GitHubOperation.Repo.FindRepo(github=github,repoName=repoName)
            if repo is None:   
                raise ValueError("ERROR!!! The repo does NOT exist!!!")
            label=repo.get_label(labelName)
            return repo.create_issue(title=title,labels=[label])
        
        @staticmethod 
        def CreateIssueWithAssignee(github
                     ,repoName:str
                     ,title:str
                     ,assignee:str
                     ):
            repo=GitHubOperation.Repo.FindRepo(github=github,repoName=repoName)
            if repo is None:   
                raise ValueError("ERROR!!! The repo does NOT exist!!!")
            return repo.create_issue(title=title,assignee=assignee)
        
        @staticmethod 
        def CreateIssueWithMilestone(github
                     ,repoName:str
                     ,title:str
                     ,milestoneName:str
                     ):
            repo=GitHubOperation.Repo.FindRepo(github=github,repoName=repoName)
            if repo is None:   
                raise ValueError("ERROR!!! The repo does NOT exist!!!")
            milestone=repo.create_milestone(milestoneName)
            return repo.create_issue(title=title,milestone=milestone)
        
        @staticmethod
        def CloseAllIssues(github
                           ,repoName:str
                           ):
            repo=GitHubOperation.Repo.FindRepo(github=github,repoName=repoName)
            if repo is None:   
                raise ValueError("ERROR!!! The repo does NOT exist!!!")
            open_issues=repo.get_issues(state="open")
            for issue in open_issues:
                issue.edit(state="closed")

    class Milestone():

        @staticmethod
        def GetMilestoneList(github
                             ,repoName:str
                             ):
            repo=GitHubOperation.Repo.FindRepo(github=github,repoName=repoName)
            if repo is None:   
                raise ValueError("ERROR!!! The repo does NOT exist!!!")
            return repo.get_milestones(state="open")
        
        @staticmethod
        def GetMilestone(github
                             ,repoName:str
                             ,number:int
                             ):
            repo=GitHubOperation.Repo.FindRepo(github=github,repoName=repoName)
            if repo is None:   
                raise ValueError("ERROR!!! The repo does NOT exist!!!")
            return repo.get_milestone(number=number)
        
        @staticmethod
        def CreateMilestone(github
                             ,repoName:str
                             ,title:str
                             ):
            repo=GitHubOperation.Repo.FindRepo(github=github,repoName=repoName)
            if repo is None:   
                raise ValueError("ERROR!!! The repo does NOT exist!!!")
            return repo.create_milestone(title=title)

        @staticmethod
        def CreateMilestoneWithStateAndDescription(github
                             ,repoName:str
                             ,title:str
                             ,state:str
                             ,description:str
                             ):
            repo=GitHubOperation.Repo.FindRepo(github=github,repoName=repoName)
            if repo is None:   
                raise ValueError("ERROR!!! The repo does NOT exist!!!")
            return repo.create_milestone(title=title,state=state,description=description)

    ## -------------------------------  ##
    # NOTICE:
    # It is NOT available.
    # Since the docs of wsgiref saids the it only support Python <= 3.2,
    # but my Python version is 3.11.2.
    # Thus, it fails to attempt to install wsgiref with pip command.
    class Webhook():

        from wsgiref.simple_server import make_server
        from pyramid.config import Configurator
        from pyramid.view import view_config, view_defaults
        from pyramid.response import Response

        ENDPOINT = "webhook"

        @view_defaults(
            route_name=ENDPOINT, renderer="json", request_method="POST"
        )
        class PayloadView(object):
            """
            View receiving of Github payload. By default, this view it's fired only if
            the request is json and method POST.
            """

            def __init__(self, request):
                self.request = request
                # Payload from Github, it's a dict
                self.payload = self.request.json

            @view_config(header="X-Github-Event:push")
            def payload_push(self):
                """This method is a continuation of PayloadView process, triggered if
                header HTTP-X-Github-Event type is Push"""
                print("No. commits in push:", len(self.payload['commits']))
                return Response("success")

            @view_config(header="X-Github-Event:pull_request")
            def payload_pull_request(self):
                """This method is a continuation of PayloadView process, triggered if
                header HTTP-X-Github-Event type is Pull Request"""
                print("PR", self.payload['action'])
                print("No. Commits in PR:", self.payload['pull_request']['commits'])

                return Response("success")

            @view_config(header="X-Github-Event:ping")
            def payload_else(self):
                print("Pinged! Webhook created with id {}!".format(self.payload["hook"]["id"]))
                return {"status": 200}


            def create_webhook():
                """ Creates a webhook for the specified repository.
                This is a programmatic approach to creating webhooks with PyGithub's API. If you wish, this can be done
                manually at your repository's page on Github in the "Settings" section. There is a option there to work with
                and configure Webhooks.
                """

                USERNAME = ""
                PASSWORD = ""
                OWNER = ""
                REPO_NAME = ""
                EVENTS = ["push", "pull_request"]
                HOST = ""

                config = {
                    "url": "http://{host}/{endpoint}".format(host=HOST, endpoint=ENDPOINT),
                    "content_type": "json"
                }

                g = Github(USERNAME, PASSWORD)
                repo = g.get_repo("{owner}/{repo_name}".format(owner=OWNER, repo_name=REPO_NAME))
                repo.create_hook("web", config, EVENTS, active=True)


        if __name__ == "__main__":
            config = Configurator()

            create_webhook()

            config.add_route(ENDPOINT, "/{}".format(ENDPOINT))
            config.scan()

        app = config.make_wsgi_app()
        server = make_server("0.0.0.0", 80, app)
        server.serve_forever()

        
        
        





def test():
    PAT="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"
    inst=GitHubOperation()
    inst.SetPAT(PAT)
    inst.ConnectGitHub()
    github=inst.GetGitHub()
    #GitHubOperation.Repo.GetAllLabelsInRepo(github=github,repoName="my-new-repo")
    #sha = data["pull_request"]["head"]["sha"]
    #GitHubOperation.Commit.CreateCommitStatusCheck(github=github,repoName="my-new-repo",state="pending",target_url="https://github.com/40843245/my-new-repo",description="description1",context="context1",sha="sha")

if __name__=='__main__':
    test()
