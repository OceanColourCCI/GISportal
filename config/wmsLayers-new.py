layers = [
   {
      "name": "cci_1",
      "options": {
         "providerShortTag": "CCI"
      },
      "services": {
         "wms": {
            "url": "https://vortices.npm.ac.uk/thredds/wms/CCI_ALL-v1.0-MONTHLY?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://vortices.npm.ac.uk/thredds/wcs/CCI_ALL-v1.0-MONTHLY?",
            "params": {
               "DescribeCoverage": {
                  "SERVICE": "WCS",
                  "request": "describeCoverage",
                  "version": "1.0.0"
               }
            }
         }
      },
      "indicators": {
         "chlor_a": {
            "niceName": "Chlorophyll-a concentration",
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Chlorophyll Indicators"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         },
         "chlor_a_bias_uncertainty": {
            "niceName": " Chlorophylla concentration uncertainty",                              
            "Confidence": "Unknown",                                  
            "interval": "Monthly",                                    
            "data_provider": "ESA Climate Change Initiative",         
            "indicator_type": [                                       
               "Chlorophyll Indicators"                                         
            ],                                                        
            "region": "Global",
            "cci_version": "Version 1.0"                                        
         },                                                           
         "chlor_a_rms_uncertainty": {
            "niceName": "Chlorophyll-a RMS uncertainty", 
            "Confidence": "Unknown", 
            "interval": "Monthly", 
            "data_provider": "ESA Climate Change Initiative", 
            "indicator_type": [ 
               "Chlorophyll Indicators" 
            ], 
            "region": "Global",
            "cci_version": "Version 1.0" 
         }, 
         "MODISA_nobs_sum": {
            "niceName": "Count of the number of observations from the MODIS (Aqua)", 
            "Confidence": "Unknown", 
            "interval": "Monthly", 
            "data_provider": "ESA Climate Change Initiative", 
            "indicator_type": [ 
               "Count of Observations" 
            ], 
            "region": "Global",
            "cci_version": "Version 1.0" 
         }, 
         "MERIS_nobs_sum": {
            "niceName": "Count of the number of observations from the MERIS sensor", 
            "Confidence": "Unknown", 
            "interval": "Monthly", 
            "data_provider": "ESA Climate Change Initiative", 
            "indicator_type": [ 
               "Count of Observations" 
            ], 
            "region": "Global",
            "cci_version": "Version 1.0" 
         }, 
         "SeaWiFS_nobs_sum": {
            "niceName": "Count of the number of observations from the SeaWiFS sensor", 
            "Confidence": "Unknown", 
            "interval": "Monthly", 
            "data_provider": "ESA Climate Change Initiative", 
            "indicator_type": [ 
               "Count of Observations" 
            ], 
            "region": "Global",
            "cci_version": "Version 1.0" 
         }, 
         "total_nobs_sum": {
            "niceName": "Count of the total number of observations", 
            "Confidence": "Unknown", 
            "interval": "Monthly", 
            "data_provider": "ESA Climate Change Initiative", 
            "indicator_type": [ 
               "Count of Observations" 
            ], 
            "region": "Global",
            "cci_version": "Version 1.0" 
         }, 
         "water_class1": {
            "niceName": "Water Class 1", 
            "Confidence": "Unknown", 
            "interval": "Monthly", 
            "data_provider": "ESA Climate Change Initiative", 
            "indicator_type": [ 
               "Water Class" 
            ], 
            "region": "Global",
            "cci_version": "Version 1.0" 
         }, 
         "water_class2": {
            "niceName": "Water Class 2", 
            "Confidence": "Unknown", 
            "interval": "Monthly", 
            "data_provider": "ESA Climate Change Initiative", 
            "indicator_type": [ 
               "Water Class" 
            ], 
            "region": "Global",
            "cci_version": "Version 1.0" 
         }, 
         "water_class3": {
            "niceName": "Water Class 3", 
            "Confidence": "Unknown", 
            "interval": "Monthly", 
            "data_provider": "ESA Climate Change Initiative", 
            "indicator_type": [ 
               "Water Class" 
            ], 
            "region": "Global",
            "cci_version": "Version 1.0" 
         }, 
         "water_class4": {
            "niceName": "Water Class 4", 
            "Confidence": "Unknown", 
            "interval": "Monthly", 
            "data_provider": "ESA Climate Change Initiative", 
            "indicator_type": [ 
               "Water Class" 
            ], 
            "region": "Global",
            "cci_version": "Version 1.0" 
         }, 
         "water_class5": {
            "niceName": "Water Class 5", 
            "Confidence": "Unknown", 
            "interval": "Monthly", 
            "data_provider": "ESA Climate Change Initiative", 
            "indicator_type": [ 
               "Water Class" 
            ], 
            "region": "Global",
            "cci_version": "Version 1.0" 
         }, 
         "water_class6": {
            "niceName": "Water Class 6", 
            "Confidence": "Unknown", 
            "interval": "Monthly", 
            "data_provider": "ESA Climate Change Initiative", 
            "indicator_type": [ 
               "Water Class" 
            ], 
            "region": "Global",
            "cci_version": "Version 1.0" 
         }, 
         "water_class7": {
            "niceName": "Water Class 7", 
            "Confidence": "Unknown", 
            "interval": "Monthly", 
            "data_provider": "ESA Climate Change Initiative", 
            "indicator_type": [ 
               "Water Class" 
            ], 
            "region": "Global",
            "cci_version": "Version 1.0" 
         }, 
         "water_class8": {
            "niceName": "Water Class 8", 
            "Confidence": "Unknown", 
            "interval": "Monthly", 
            "data_provider": "ESA Climate Change Initiative", 
            "indicator_type": [ 
               "Water Class" 
            ], 
            "region": "Global",
            "cci_version": "Version 1.0" 
         }, 
         "water_class9": {
            "niceName": "Water Class 9", 
            "Confidence": "Unknown", 
            "interval": "Monthly", 
            "data_provider": "ESA Climate Change Initiative", 
            "indicator_type": [ 
               "Water Class" 
            ], 
            "region": "Global",
            "cci_version": "Version 1.0" 
         }, 
         "aph_412": {
            "niceName": "aph_412", 
            "Confidence": "Unknown", 
            "interval": "Monthly", 
            "data_provider": "ESA Climate Change Initiative", 
            "indicator_type": [ 
               "Ocean Colour" 
            ], 
            "region": "Global",
            "cci_version": "Version 1.0" 
         }, 
         "aph_443": {
            "niceName": "aph_443", 
            "Confidence": "Unknown", 
            "interval": "Monthly", 
            "data_provider": "ESA Climate Change Initiative", 
            "indicator_type": [ 
               "Ocean Colour" 
            ], 
            "region": "Global",
            "cci_version": "Version 1.0" 
         }, 
         "aph_490": {
            "niceName": "aph_490", 
            "Confidence": "Unknown", 
            "interval": "Monthly", 
            "data_provider": "ESA Climate Change Initiative", 
            "indicator_type": [ 
               "Ocean Colour" 
            ], 
            "region": "Global",
            "cci_version": "Version 1.0" 
         }, 
         "aph_510": {
            "niceName": "aph_510", 
            "Confidence": "Unknown", 
            "interval": "Monthly", 
            "data_provider": "ESA Climate Change Initiative", 
            "indicator_type": [ 
               "Ocean Colour" 
            ], 
            "region": "Global",
            "cci_version": "Version 1.0" 
         }, 
         "aph_555": {
            "niceName": "aph_555", 
            "Confidence": "Unknown", 
            "interval": "Monthly", 
            "data_provider": "ESA Climate Change Initiative", 
            "indicator_type": [ 
               "Ocean Colour" 
            ], 
            "region": "Global",
            "cci_version": "Version 1.0" 
         }, 
         "aph_670": {
            "niceName": "aph_670", 
            "Confidence": "Unknown", 
            "interval": "Monthly", 
            "data_provider": "ESA Climate Change Initiative", 
            "indicator_type": [ 
               "Ocean Colour" 
            ], 
            "region": "Global",
            "cci_version": "Version 1.0" 
         }, 
         "atot_412": {
            "niceName": "Total absorption coefficient",
            "wavelength": "412 nm", 
            "Confidence": "Unknown", 
            "interval": "Monthly", 
            "data_provider": "ESA Climate Change Initiative", 
            "indicator_type": [ 
               "Inherent Optical Properties (IOPs)" 
            ], 
            "region": "Global",
            "cci_version": "Version 1.0" 
         }, 
         "atot_443": {
            "niceName": "Total absorption coefficient",
            "wavelength": "443 nm", 
            "Confidence": "Unknown", 
            "interval": "Monthly", 
            "data_provider": "ESA Climate Change Initiative", 
            "indicator_type": [ 
               "Inherent Optical Properties (IOPs)" 
            ], 
            "region": "Global",
            "cci_version": "Version 1.0" 
         }, 
         "atot_490": {
            "niceName": "Total absorption coefficient",
            "wavelength": "490 nm", 
            "Confidence": "Unknown", 
            "interval": "Monthly", 
            "data_provider": "ESA Climate Change Initiative", 
            "indicator_type": [ 
               "Inherent Optical Properties (IOPs)" 
            ], 
            "region": "Global",
            "cci_version": "Version 1.0" 
         }, 
         "atot_510": {
            "niceName": "Total absorption coefficient",
            "wavelength": "510 nm", 
            "Confidence": "Unknown", 
            "interval": "Monthly", 
            "data_provider": "ESA Climate Change Initiative", 
            "indicator_type": [ 
               "Inherent Optical Properties (IOPs)" 
            ], 
            "region": "Global",
            "cci_version": "Version 1.0" 
         }, 
         "atot_555": {
            "niceName": "Total absorption coefficient",
            "wavelength": "555 nm", 
            "Confidence": "Unknown", 
            "interval": "Monthly", 
            "data_provider": "ESA Climate Change Initiative", 
            "indicator_type": [ 
               "Inherent Optical Properties (IOPs)" 
            ], 
            "region": "Global",
            "cci_version": "Version 1.0" 
         }, 
         "atot_670": {
            "niceName": "Total absorption coefficient",
            "wavelength": "670 nm", 
            "Confidence": "Unknown", 
            "interval": "Monthly", 
            "data_provider": "ESA Climate Change Initiative", 
            "indicator_type": [ 
               "Inherent Optical Properties (IOPs)" 
            ], 
            "region": "Global",
            "cci_version": "Version 1.0" 
         }, 
         "adg_412": {
            "niceName": "adg_412", 
            "Confidence": "Unknown", 
            "interval": "Monthly", 
            "data_provider": "ESA Climate Change Initiative", 
            "indicator_type": [ 
               "Ocean Colour" 
            ], 
            "region": "Global",
            "cci_version": "Version 1.0" 
         }, 
         "adg_443": {
            "niceName": "adg_443", 
            "Confidence": "Unknown", 
            "interval": "Monthly", 
            "data_provider": "ESA Climate Change Initiative", 
            "indicator_type": [ 
               "Ocean Colour" 
            ], 
            "region": "Global",
            "cci_version": "Version 1.0" 
         }, 
         "adg_490": {
            "niceName": "adg_490", 
            "Confidence": "Unknown", 
            "interval": "Monthly", 
            "data_provider": "ESA Climate Change Initiative", 
            "indicator_type": [ 
               "Ocean Colour" 
            ], 
            "region": "Global",
            "cci_version": "Version 1.0" 
         }, 
         "adg_510": {
            "niceName": "adg_510", 
            "Confidence": "Unknown", 
            "interval": "Monthly", 
            "data_provider": "ESA Climate Change Initiative", 
            "indicator_type": [ 
               "Ocean Colour" 
            ], 
            "region": "Global",
            "cci_version": "Version 1.0" 
         }, 
         "adg_555": {
            "niceName": "adg_555", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "adg_670": {
            "niceName": "adg_670", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "bbp_412": {
            "niceName": "bbp_412", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "bbp_443": {
            "niceName": "bbp_443", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "bbp_490": {
            "niceName": "bbp_490", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "bbp_510": {
            "niceName": "bbp_510", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "bbp_555": {
            "niceName": "bbp_555", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "bbp_670": {
            "niceName": "bbp_670", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "Rrs_412": {
            "niceName": "Rrs_412", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "Rrs_443": {
            "niceName": "Rrs_443", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "Rrs_490": {
            "niceName": "Rrs_490", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "Rrs_510": {
            "niceName": "Rrs_510", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "Rrs_555": {
            "niceName": "Rrs_555", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "Rrs_670": {
            "niceName": "Rrs_670", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "kd_490": {
            "niceName": "kd_490", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "aph_412_bias_uncertainty": {
            "niceName": "aph_412_bias_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "aph_443_bias_uncertainty": {
            "niceName": "aph_443_bias_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "aph_490_bias_uncertainty": {
            "niceName": "aph_490_bias_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "aph_510_bias_uncertainty": {
            "niceName": "aph_510_bias_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "aph_555_bias_uncertainty": {
            "niceName": "aph_555_bias_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "aph_670_bias_uncertainty": {
            "niceName": "aph_670_bias_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "adg_412_bias_uncertainty": {
            "niceName": "adg_412_bias_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "adg_443_bias_uncertainty": {
            "niceName": "adg_443_bias_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "adg_490_bias_uncertainty": {
            "niceName": "adg_490_bias_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "adg_510_bias_uncertainty": {
            "niceName": "adg_510_bias_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "adg_555_bias_uncertainty": {
            "niceName": "adg_555_bias_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "adg_670_bias_uncertainty": {
            "niceName": "adg_670_bias_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "Rrs_412_bias_uncertainty": {
            "niceName": "Rrs_412_bias_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "Rrs_443_bias_uncertainty": {
            "niceName": "Rrs_443_bias_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "Rrs_490_bias_uncertainty": {
            "niceName": "Rrs_490_bias_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "Rrs_510_bias_uncertainty": {
            "niceName": "Rrs_510_bias_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "Rrs_555_bias_uncertainty": {
            "niceName": "Rrs_555_bias_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "Rrs_670_bias_uncertainty": {
            "niceName": "Rrs_670_bias_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "kd_490_bias_uncertainty": {
            "niceName": "kd_490_bias_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "aph_412_rms_uncertainty": {
            "niceName": "aph_412_rms_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "aph_443_rms_uncertainty": {
            "niceName": "aph_443_rms_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "aph_490_rms_uncertainty": {
            "niceName": "aph_490_rms_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "aph_510_rms_uncertainty": {
            "niceName": "aph_510_rms_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "aph_555_rms_uncertainty": {
            "niceName": "aph_555_rms_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "aph_670_rms_uncertainty": {
            "niceName": "aph_670_rms_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "adg_412_rms_uncertainty": {
            "niceName": "adg_412_rms_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "adg_443_rms_uncertainty": {
            "niceName": "adg_443_rms_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "adg_490_rms_uncertainty": {
            "niceName": "adg_490_rms_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "adg_510_rms_uncertainty": {
            "niceName": "adg_510_rms_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "adg_555_rms_uncertainty": {
            "niceName": "adg_555_rms_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "adg_670_rms_uncertainty": {
            "niceName": "adg_670_rms_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "Rrs_412_rms_uncertainty": {
            "niceName": "Rrs_412_rms_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "Rrs_443_rms_uncertainty": {
            "niceName": "Rrs_443_rms_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "Rrs_490_rms_uncertainty": {
            "niceName": "Rrs_490_rms_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "Rrs_510_rms_uncertainty": {
            "niceName": "Rrs_510_rms_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "Rrs_555_rms_uncertainty": {
            "niceName": "Rrs_555_rms_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "Rrs_670_rms_uncertainty": {
            "niceName": "Rrs_670_rms_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 
         "kd_490_rms_uncertainty": {
            "niceName": "kd_490_rms_uncertainty", 
            "Confidence": "Unknown",
            "interval": "Monthly",
            "data_provider": "ESA Climate Change Initiative",
            "indicator_type": [
               "Ocean Colour"
            ],
            "region": "Global",
            "cci_version": "Version 1.0"
         }, 

      }
   }
]
