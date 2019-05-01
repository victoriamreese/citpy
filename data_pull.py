from panoptes_client import Panoptes, Project, SubjectSet, Classification

#this script will pull data from zooniverse project

#authentication:
owner = Panoptes.connect(username='fakeuser', password='fakepwd')

with owner:
    all_proj_classifications = Classification.where(scope='project', project_id=3866)

#returns ResultPaginator Object that we can iterate through and pull out new values
#can I use this for my web app? would need to reinvision scripts

#could write script to iterate through only select date range
#need datetime for that, probably


    for i in iter(all_proj_classifications):
        print(i)

