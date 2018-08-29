
Productions = { 
   
   'summer16_nAOD_v1' : {
                          'isData'  : False ,
                          'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/summer16_nAOD_v1.py' ,
                          'cmssw'   : 'Full2016' ,  
                        },

   'summer16_nAOD_v1_test' : {
                          'isData'  : False ,
                          'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/summer16_nAOD_v1_test.py' ,
                          'cmssw'   : 'Full2016' ,
                        },                    

   'Run2017_nAOD_v1_Study2017':  {
                         'isData'  : True ,
                         'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt"  % os.environ["CMSSW_BASE"]',
                         'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2017_nAOD_v1.py' ,
                         'cmssw'   : 'Study2017' ,
                   },

   'Fall2017_nAOD_v1_Study2017':  {
                         'isData'  : False ,
                         'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/fall17_nAOD_v1.py' ,
                         'cmssw'   : 'Study2017' ,
                   },               


   'Run2017_nAOD_v1_Full2017':  {
                         'isData'  : True ,
                         'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt"  % os.environ["CMSSW_BASE"]',
                         'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2017_nAOD_v1.py' ,
                         'cmssw'   : 'Full2017' ,
                   },

   'Fall2017_nAOD_v1_Full2017':  {
                         'isData'  : False ,
                         'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/fall17_nAOD_v1.py' ,
                         'cmssw'   : 'Full2017' ,
                   },                

}