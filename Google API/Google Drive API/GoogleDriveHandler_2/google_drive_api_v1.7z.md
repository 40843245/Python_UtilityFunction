# google_drive_api_v1.7z.md
## Prequisite
1. Install these dependency
2. Do the quickstart guide.
## Dependency
1. pickle
2. google
3. googleapiclient
4. tabulate
5. pandas

## Quickstart Guide
### Part 1
First, we need to create a(n) credentials. To do that, follow the following steps:
1. Create a(n) credentials.
2. Download it.
3. Rename it as credentials.json.
4. Move it to the working directory.

## API
### get_gdrive_service
  @staticmethod
  def get_gdrive_service()
### list_files
  @staticmethod
  def list_files(items) -> list | str | None
### get_folder_id
  @staticmethod
  def get_folder_id(folder_name:str):

## More details
For more details about API, see the comments on the source code located at google_drive_api_v1.7z.

## Ref
### Code
Some pieces of code are modified from 

https://www.bing.com/search?q=google%20drive%20API%20python&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=google%20drive%20api%20pytho&sc=11-22&sk=&cvid=FFA05DABA8F646E7AA3999AB8C3889AC&ghsh=0&ghacc=0&ghpl=
