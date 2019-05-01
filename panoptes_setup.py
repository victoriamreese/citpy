from panoptes_client import exportable, Panoptes, Project, SubjectSet, Subject, Classification
import pandas as pd

Panoptes.connect(username='reesevic000', password='Scoop123!')


Panoptes.connect(client_id='a24a23500871c12b6dd007e926d8c74b8147ba9f0004299ccdde89b942ad02eb', client_secret='32ea4c175c13c4907be32626969e2b5823f1206dcda069781194f906a1628f82')

project = Project.find('3866')

print(project.title)


#https://panoptes-staging.zooniverse.org/api/classifications?project_id=3866


classification_export = Project(3866).get_export('classifications')
for row in classification_export.csv_dictreader():
    print(row['user_id'])

