import os
import os.path
import pandas as pd
import synapseclient
from synapseclient import Project, Folder, File, Link

download_path = '/Users/spanglry/Data/tcga'

# login
syn = synapseclient.Synapse()
syn.login('spanglry', '11tree11')

# get clinical and gene expression files from TCGA Live
results = syn.chunkedQuery("select id, name, acronym from entity where entity.benefactorId=='syn2812961'")

for res in results:
  # if '_bio.' in name or 'V2.geneExp' in name and '.ttl' not in name:
  # if 'V2.geneExp' in name:
  name = res['entity.name']
  if os.path.isfile(download_path + name):
    print name + " exists!"
  else:
    #print res['entity.acronym'][0], res['entity.id'], name
    try:
      en = syn.get(res['entity.id'], downloadLocation=download_path)
    except:
      print "Downloading " + name + " failed!"

