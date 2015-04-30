layers = [
   {
      "name": "cci_1m",
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
            "niceName": "Chlorophyll-a Concentration",
            "interval": "Monthly",
            "indicator_type": [
               "Chlorophyll Indicators"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "chlor_a_bias_uncertainty": {
            "niceName": " Chlorophyll-a Concentration uncertainty",
            "interval": "Monthly",
                        "indicator_type": [                                       
               "Chlorophyll Indicators"                                         
            ],
            "cci_version": "Version 1.0"                                        
         },
         "chlor_a_rms_uncertainty": {
            "niceName": "Chlorophyll-a RMS uncertainty",
            "interval": "Monthly",
                        "indicator_type": [ 
               "Chlorophyll Indicators" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "MODISA_nobs_sum": {
            "niceName": "Count of the number of observations from the MODIS (Aqua)",
            "interval": "Monthly",
                        "indicator_type": [ 
               "Count of Observations" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "MERIS_nobs_sum": {
            "niceName": "Count of the number of observations from the MERIS sensor",
            "interval": "Monthly",
                        "indicator_type": [ 
               "Count of Observations" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "SeaWiFS_nobs_sum": {
            "niceName": "Count of the number of observations from the SeaWiFS sensor",
            "interval": "Monthly",
                        "indicator_type": [ 
               "Count of Observations" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "total_nobs_sum": {
            "niceName": "Count of the total number of observations",
            "interval": "Monthly",
                        "indicator_type": [ 
               "Count of Observations" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "water_class1": {
            "niceName": "Water Class 1",
            "interval": "Monthly",
                        "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "water_class2": {
            "niceName": "Water Class 2",
            "interval": "Monthly",
                        "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "water_class3": {
            "niceName": "Water Class 3",
            "interval": "Monthly",
                        "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "water_class4": {
            "niceName": "Water Class 4",
            "interval": "Monthly",
                        "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "water_class5": {
            "niceName": "Water Class 5",
            "interval": "Monthly",
                        "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "water_class6": {
            "niceName": "Water Class 6",
            "interval": "Monthly",
                        "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "water_class7": {
            "niceName": "Water Class 7",
            "interval": "Monthly",
                        "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "water_class8": {
            "niceName": "Water Class 8",
            "interval": "Monthly",
                        "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "water_class9": {
            "niceName": "Water Class 9",
            "interval": "Monthly",
                        "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "aph_412": {
            "niceName": "Phytoplankton absorption coefficient",
            "wavelength": "412 nm",
            "interval": "Monthly",
                        "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "aph_443": {
            "niceName": "Phytoplankton absorption coefficient",
            "wavelength": "443 nm",
            "interval": "Monthly",
                        "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "aph_490": {
            "niceName": "Phytoplankton absorption coefficient",
            "wavelength": "490 nm",
            "interval": "Monthly",
                        "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "aph_510": {
            "niceName": "Phytoplankton absorption coefficient",
            "wavelength": "510 nm",
            "interval": "Monthly",
                        "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "aph_555": {
            "niceName": "Phytoplankton absorption coefficient",
            "wavelength": "555 nm",
            "interval": "Monthly",
                        "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "aph_670": {
            "niceName": "Phytoplankton absorption coefficient",
            "wavelength": "670 nm",
            "interval": "Monthly",
                        "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "atot_412": {
            "niceName": "Total absorption coefficient",
            "wavelength": "412 nm",
            "interval": "Monthly",
                        "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "atot_443": {
            "niceName": "Total absorption coefficient",
            "wavelength": "443 nm",
            "interval": "Monthly",
                        "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "atot_490": {
            "niceName": "Total absorption coefficient",
            "wavelength": "490 nm",
            "interval": "Monthly",
                        "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "atot_510": {
            "niceName": "Total absorption coefficient",
            "wavelength": "510 nm",
            "interval": "Monthly",
                        "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "atot_555": {
            "niceName": "Total absorption coefficient",
            "wavelength": "555 nm",
            "interval": "Monthly",
                        "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "atot_670": {
            "niceName": "Total absorption coefficient",
            "wavelength": "670 nm",
            "interval": "Monthly",
                        "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "adg_412": {
            "niceName": "Absorption coefficient for dissolved and detrital material",
            "wavelength": "412 nm",
            "interval": "Monthly",
                        "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "adg_443": {
            "niceName": "Absorption coefficient for dissolved and detrital material",
            "wavelength": "443 nm",
            "interval": "Monthly",
                        "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "adg_490": {
            "niceName": "Absorption coefficient for dissolved and detrital material",
            "wavelength": "490 nm",
            "interval": "Monthly",
                        "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "adg_510": {
            "niceName": "Absorption coefficient for dissolved and detrital material",
            "wavelength": "510 nm",
            "interval": "Monthly",
                        "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "adg_555": {
            "niceName": "Absorption coefficient for dissolved and detrital material",
            "wavelength": "555 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "adg_670": {
            "niceName": "Absorption coefficient for dissolved and detrital material",
            "wavelength": "670 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "bbp_412": {
            "niceName": "Particulate backscattering coefficient for dissolved and detrital material",
            "wavelength": "412 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "bbp_443": {
            "niceName": "Particulate backscattering coefficient for dissolved and detrital material",
            "wavelength": "443 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "bbp_490": {
            "niceName": "Particulate backscattering coefficient for dissolved and detrital material",
            "wavelength": "490 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "bbp_510": {
            "niceName": "Particulate backscattering coefficient for dissolved and detrital material",
            "wavelength": "510 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "bbp_555": {
            "niceName": "Particulate backscattering coefficient for dissolved and detrital material",
            "wavelength": "555 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "bbp_670": {
            "niceName": "Particulate backscattering coefficient for dissolved and detrital material",
            "wavelength": "670 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_412": {
            "niceName": "Remote sensing reflectance",
            "wavelength": "412 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_443": {
            "niceName": "Remote sensing reflectance",
            "wavelength": "443 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_490": {
            "niceName": "Remote sensing reflectance",
            "wavelength": "490 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_510": {
            "niceName": "Remote sensing reflectance",
            "wavelength": "510 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_555": {
            "niceName": "Remote sensing reflectance",
            "wavelength": "555 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_670": {
            "niceName": "Remote sensing reflectance",
            "wavelength": "670 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "kd_490": {
            "niceName": "Downwelling attenuation coefficient at 490nm",
            "interval": "Monthly",
            "indicator_type": [
               "Water Turbidity Indicators"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "aph_412_bias_uncertainty": {
            "niceName": "Phytoplankton absorption coefficient uncertainty",
            "wavelength": "412 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "aph_443_bias_uncertainty": {
            "niceName": "Phytoplankton absorption coefficient uncertainty",
            "wavelength": "443 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "aph_490_bias_uncertainty": {
            "niceName": "Phytoplankton absorption coefficient uncertainty",
            "wavelength": "490 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "aph_510_bias_uncertainty": {
            "niceName": "Phytoplankton absorption coefficient uncertainty",
            "wavelength": "510 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "aph_555_bias_uncertainty": {
            "niceName": "Phytoplankton absorption coefficient uncertainty",
            "wavelength": "555 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "aph_670_bias_uncertainty": {
            "niceName": "Phytoplankton absorption coefficient uncertainty",
            "wavelength": "670 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "adg_412_bias_uncertainty": {
            "niceName": "Absorption coefficient for dissolved and detrital material uncertainty",
            "wavelength": "412 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "adg_443_bias_uncertainty": {
            "niceName": "Absorption coefficient for dissolved and detrital material uncertainty",
            "wavelength": "443 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "adg_490_bias_uncertainty": {
            "niceName": "Absorption coefficient for dissolved and detrital material uncertainty",
            "wavelength": "490 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "adg_510_bias_uncertainty": {
            "niceName": "Absorption coefficient for dissolved and detrital material uncertainty",
            "wavelength": "510 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "adg_555_bias_uncertainty": {
            "niceName": "Absorption coefficient for dissolved and detrital material uncertainty",
            "wavelength": "555 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "adg_670_bias_uncertainty": {
            "niceName": "Absorption coefficient for dissolved and detrital material uncertainty",
            "wavelength": "670 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_412_bias_uncertainty": {
            "niceName": "Remote sensing reflectance uncertainty",
            "wavelength": "412 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_443_bias_uncertainty": {
            "niceName": "Remote sensing reflectance uncertainty",
            "wavelength": "443 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_490_bias_uncertainty": {
            "niceName": "Remote sensing reflectance uncertainty",
            "wavelength": "490 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_510_bias_uncertainty": {
            "niceName": "Remote sensing reflectance uncertainty",
            "wavelength": "510 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_555_bias_uncertainty": {
            "niceName": "Remote sensing reflectance uncertainty",
            "wavelength": "555 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_670_bias_uncertainty": {
            "niceName": "Remote sensing reflectance uncertainty",
            "wavelength": "670 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "kd_490_bias_uncertainty": {
            "niceName": "Downwelling attenuation coefficient at 490nm uncertainty",
            "interval": "Monthly",
            "indicator_type": [
               "Water Turbidity Indicators"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "aph_412_rms_uncertainty": {
            "niceName": "Phytoplankton absorption coefficient RMS uncertainty",
            "wavelength": "412 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "aph_443_rms_uncertainty": {
            "niceName": "Phytoplankton absorption coefficient RMS uncertainty",
            "wavelength": "443 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "aph_490_rms_uncertainty": {
            "niceName": "Phytoplankton absorption coefficient RMS uncertainty",
            "wavelength": "490 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "aph_510_rms_uncertainty": {
            "niceName": "Phytoplankton absorption coefficient RMS uncertainty",
            "wavelength": "510 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "aph_555_rms_uncertainty": {
            "niceName": "Phytoplankton absorption coefficient RMS uncertainty",
            "wavelength": "555 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "aph_670_rms_uncertainty": {
            "niceName": "Phytoplankton absorption coefficient RMS uncertainty",
            "wavelength": "670 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "adg_412_rms_uncertainty": {
            "niceName": "Absorption coefficient for dissolved and detrital material RMS uncertainty",
            "wavelength": "412 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "adg_443_rms_uncertainty": {
            "niceName": "Absorption coefficient for dissolved and detrital material RMS uncertainty",
            "wavelength": "443 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "adg_490_rms_uncertainty": {
            "niceName": "Absorption coefficient for dissolved and detrital material RMS uncertainty",
            "wavelength": "490 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "adg_510_rms_uncertainty": {
            "niceName": "Absorption coefficient for dissolved and detrital material RMS uncertainty",
            "wavelength": "510 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "adg_555_rms_uncertainty": {
            "niceName": "Absorption coefficient for dissolved and detrital material RMS uncertainty",
            "wavelength": "555 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "adg_670_rms_uncertainty": {
            "niceName": "Absorption coefficient for dissolved and detrital material RMS uncertainty",
            "wavelength": "670 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_412_rms_uncertainty": {
            "niceName": "Remote sensing reflectance RMS uncertainty",
            "wavelength": "412 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_443_rms_uncertainty": {
            "niceName": "Remote sensing reflectance RMS uncertainty",
            "wavelength": "443 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_490_rms_uncertainty": {
            "niceName": "Remote sensing reflectance RMS uncertainty",
            "wavelength": "490 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_510_rms_uncertainty": {
            "niceName": "Remote sensing reflectance RMS uncertainty",
            "wavelength": "510 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_555_rms_uncertainty": {
            "niceName": "Remote sensing reflectance RMS uncertainty",
            "wavelength": "555 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_670_rms_uncertainty": {
            "niceName": "Remote sensing reflectance RMS uncertainty",
            "wavelength": "670 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "kd_490_rms_uncertainty": {
            "niceName": "Downwelling attenuation coefficient at 490nm RMS uncertainty",
            "interval": "Monthly",
            "indicator_type": [
               "Water Turbidity Indicators"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },

      }
   },
   {
      "name": "cci_1d",
      "options": {
         "providerShortTag": "CCI"
      },
      "services": {
         "wms": {
            "url": "https://vortices.npm.ac.uk/thredds/wms/CCI_ALL-v1.0-DAILY?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://vortices.npm.ac.uk/thredds/wcs/CCI_ALL-v1.0-DAILY?",
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
            "niceName": "Chlorophyll-a Concentration",
            "interval": "Daily",
            "indicator_type": [
               "Chlorophyll Indicators"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "chlor_a_bias_uncertainty": {
            "niceName": " Chlorophyll-a Concentration uncertainty",
            "interval": "Daily",
            "indicator_type": [                                       
               "Chlorophyll Indicators"                                         
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"                                        
         },
         "chlor_a_rms_uncertainty": {
            "niceName": "Chlorophyll-a RMS uncertainty",
            "interval": "Daily",
            "indicator_type": [ 
               "Chlorophyll Indicators" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "MODISA_nobs": {
            "niceName": "Count of the number of observations from the MODIS (Aqua)",
            "interval": "Daily",
            "indicator_type": [ 
               "Count of Observations" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "MERIS_nobs": {
            "niceName": "Count of the number of observations from the MERIS sensor",
            "interval": "Daily",
            "indicator_type": [ 
               "Count of Observations" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "SeaWiFS_nobs": {
            "niceName": "Count of the number of observations from the SeaWiFS sensor",
            "interval": "Daily",
            "indicator_type": [ 
               "Count of Observations" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "total_nobs": {
            "niceName": "Count of the total number of observations",
            "interval": "Daily",
            "indicator_type": [ 
               "Count of Observations" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "water_class1": {
            "niceName": "Water Class 1",
            "interval": "Daily",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "water_class2": {
            "niceName": "Water Class 2",
            "interval": "Daily",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "water_class3": {
            "niceName": "Water Class 3",
            "interval": "Daily",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "water_class4": {
            "niceName": "Water Class 4",
            "interval": "Daily",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "water_class5": {
            "niceName": "Water Class 5",
            "interval": "Daily",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "water_class6": {
            "niceName": "Water Class 6",
            "interval": "Daily",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "water_class7": {
            "niceName": "Water Class 7",
            "interval": "Daily",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "water_class8": {
            "niceName": "Water Class 8",
            "interval": "Daily",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "water_class9": {
            "niceName": "Water Class 9",
            "interval": "Daily",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "aph_412": {
            "niceName": "Phytoplankton absorption coefficient",
            "wavelength": "412 nm",
            "interval": "Daily",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "aph_443": {
            "niceName": "Phytoplankton absorption coefficient",
            "wavelength": "443 nm",
            "interval": "Daily",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "aph_490": {
            "niceName": "Phytoplankton absorption coefficient",
            "wavelength": "490 nm",
            "interval": "Daily",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "aph_510": {
            "niceName": "Phytoplankton absorption coefficient",
            "wavelength": "510 nm",
            "interval": "Daily",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "aph_555": {
            "niceName": "Phytoplankton absorption coefficient",
            "wavelength": "555 nm",
            "interval": "Daily",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "aph_670": {
            "niceName": "Phytoplankton absorption coefficient",
            "wavelength": "670 nm",
            "interval": "Daily",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "atot_412": {
            "niceName": "Total absorption coefficient",
            "wavelength": "412 nm",
            "interval": "Daily",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "atot_443": {
            "niceName": "Total absorption coefficient",
            "wavelength": "443 nm",
            "interval": "Daily",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "atot_490": {
            "niceName": "Total absorption coefficient",
            "wavelength": "490 nm",
            "interval": "Daily",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "atot_510": {
            "niceName": "Total absorption coefficient",
            "wavelength": "510 nm",
            "interval": "Daily",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "atot_555": {
            "niceName": "Total absorption coefficient",
            "wavelength": "555 nm",
            "interval": "Daily",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "atot_670": {
            "niceName": "Total absorption coefficient",
            "wavelength": "670 nm",
            "interval": "Daily",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "adg_412": {
            "niceName": "Absorption coefficient for dissolved and detrital material",
            "wavelength": "412 nm",
            "interval": "Daily",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "adg_443": {
            "niceName": "Absorption coefficient for dissolved and detrital material",
            "wavelength": "443 nm",
            "interval": "Daily",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "adg_490": {
            "niceName": "Absorption coefficient for dissolved and detrital material",
            "wavelength": "490 nm",
            "interval": "Daily",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "adg_510": {
            "niceName": "Absorption coefficient for dissolved and detrital material",
            "wavelength": "510 nm",
            "interval": "Daily",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0" 
         },
         "adg_555": {
            "niceName": "Absorption coefficient for dissolved and detrital material",
            "wavelength": "555 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "adg_670": {
            "niceName": "Absorption coefficient for dissolved and detrital material",
            "wavelength": "670 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "bbp_412": {
            "niceName": "Particulate backscattering coefficient for dissolved and detrital material",
            "wavelength": "412 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "bbp_443": {
            "niceName": "Particulate backscattering coefficient for dissolved and detrital material",
            "wavelength": "443 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "bbp_490": {
            "niceName": "Particulate backscattering coefficient for dissolved and detrital material",
            "wavelength": "490 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "bbp_510": {
            "niceName": "Particulate backscattering coefficient for dissolved and detrital material",
            "wavelength": "510 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "bbp_555": {
            "niceName": "Particulate backscattering coefficient for dissolved and detrital material",
            "wavelength": "555 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "bbp_670": {
            "niceName": "Particulate backscattering coefficient for dissolved and detrital material",
            "wavelength": "670 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_412": {
            "niceName": "Remote sensing reflectance",
            "wavelength": "412 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_443": {
            "niceName": "Remote sensing reflectance",
            "wavelength": "443 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_490": {
            "niceName": "Remote sensing reflectance",
            "wavelength": "490 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_510": {
            "niceName": "Remote sensing reflectance",
            "wavelength": "510 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_555": {
            "niceName": "Remote sensing reflectance",
            "wavelength": "555 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_670": {
            "niceName": "Remote sensing reflectance",
            "wavelength": "670 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "kd_490": {
            "niceName": "Downwelling attenuation coefficient at 490nm",
            "interval": "Daily",
            "indicator_type": [
               "Water Turbidity Indicators"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "aph_412_bias_uncertainty": {
            "niceName": "Phytoplankton absorption coefficient uncertainty",
            "wavelength": "412 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "aph_443_bias_uncertainty": {
            "niceName": "Phytoplankton absorption coefficient uncertainty",
            "wavelength": "443 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "aph_490_bias_uncertainty": {
            "niceName": "Phytoplankton absorption coefficient uncertainty",
            "wavelength": "490 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "aph_510_bias_uncertainty": {
            "niceName": "Phytoplankton absorption coefficient uncertainty",
            "wavelength": "510 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "aph_555_bias_uncertainty": {
            "niceName": "Phytoplankton absorption coefficient uncertainty",
            "wavelength": "555 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "aph_670_bias_uncertainty": {
            "niceName": "Phytoplankton absorption coefficient uncertainty",
            "wavelength": "670 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "adg_412_bias_uncertainty": {
            "niceName": "Absorption coefficient for dissolved and detrital material uncertainty",
            "wavelength": "412 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "adg_443_bias_uncertainty": {
            "niceName": "Absorption coefficient for dissolved and detrital material uncertainty",
            "wavelength": "443 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "adg_490_bias_uncertainty": {
            "niceName": "Absorption coefficient for dissolved and detrital material uncertainty",
            "wavelength": "490 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "adg_510_bias_uncertainty": {
            "niceName": "Absorption coefficient for dissolved and detrital material uncertainty",
            "wavelength": "510 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "adg_555_bias_uncertainty": {
            "niceName": "Absorption coefficient for dissolved and detrital material uncertainty",
            "wavelength": "555 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "adg_670_bias_uncertainty": {
            "niceName": "Absorption coefficient for dissolved and detrital material uncertainty",
            "wavelength": "670 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_412_bias_uncertainty": {
            "niceName": "Remote sensing reflectance uncertainty",
            "wavelength": "412 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_443_bias_uncertainty": {
            "niceName": "Remote sensing reflectance uncertainty",
            "wavelength": "443 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_490_bias_uncertainty": {
            "niceName": "Remote sensing reflectance uncertainty",
            "wavelength": "490 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_510_bias_uncertainty": {
            "niceName": "Remote sensing reflectance uncertainty",
            "wavelength": "510 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_555_bias_uncertainty": {
            "niceName": "Remote sensing reflectance uncertainty",
            "wavelength": "555 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_670_bias_uncertainty": {
            "niceName": "Remote sensing reflectance uncertainty",
            "wavelength": "670 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "kd_490_bias_uncertainty": {
            "niceName": "Downwelling attenuation coefficient at 490nm uncertainty",
            "interval": "Daily",
            "indicator_type": [
               "Water Turbidity Indicators"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "aph_412_rms_uncertainty": {
            "niceName": "Phytoplankton absorption coefficient RMS uncertainty",
            "wavelength": "412 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "aph_443_rms_uncertainty": {
            "niceName": "Phytoplankton absorption coefficient RMS uncertainty",
            "wavelength": "443 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "aph_490_rms_uncertainty": {
            "niceName": "Phytoplankton absorption coefficient RMS uncertainty",
            "wavelength": "490 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "aph_510_rms_uncertainty": {
            "niceName": "Phytoplankton absorption coefficient RMS uncertainty",
            "wavelength": "510 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "aph_555_rms_uncertainty": {
            "niceName": "Phytoplankton absorption coefficient RMS uncertainty",
            "wavelength": "555 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "aph_670_rms_uncertainty": {
            "niceName": "Phytoplankton absorption coefficient RMS uncertainty",
            "wavelength": "670 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "adg_412_rms_uncertainty": {
            "niceName": "Absorption coefficient for dissolved and detrital material RMS uncertainty",
            "wavelength": "412 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "adg_443_rms_uncertainty": {
            "niceName": "Absorption coefficient for dissolved and detrital material RMS uncertainty",
            "wavelength": "443 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "adg_490_rms_uncertainty": {
            "niceName": "Absorption coefficient for dissolved and detrital material RMS uncertainty",
            "wavelength": "490 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "adg_510_rms_uncertainty": {
            "niceName": "Absorption coefficient for dissolved and detrital material RMS uncertainty",
            "wavelength": "510 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "adg_555_rms_uncertainty": {
            "niceName": "Absorption coefficient for dissolved and detrital material RMS uncertainty",
            "wavelength": "555 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "adg_670_rms_uncertainty": {
            "niceName": "Absorption coefficient for dissolved and detrital material RMS uncertainty",
            "wavelength": "670 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_412_rms_uncertainty": {
            "niceName": "Remote sensing reflectance RMS uncertainty",
            "wavelength": "412 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_443_rms_uncertainty": {
            "niceName": "Remote sensing reflectance RMS uncertainty",
            "wavelength": "443 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_490_rms_uncertainty": {
            "niceName": "Remote sensing reflectance RMS uncertainty",
            "wavelength": "490 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_510_rms_uncertainty": {
            "niceName": "Remote sensing reflectance RMS uncertainty",
            "wavelength": "510 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_555_rms_uncertainty": {
            "niceName": "Remote sensing reflectance RMS uncertainty",
            "wavelength": "555 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "Rrs_670_rms_uncertainty": {
            "niceName": "Remote sensing reflectance RMS uncertainty",
            "wavelength": "670 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },
         "kd_490_rms_uncertainty": {
            "niceName": "Downwelling attenuation coefficient at 490nm RMS uncertainty",
            "interval": "Daily",
            "indicator_type": [
               "Water Turbidity Indicators"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 1.0"
         },

      }
   },
   {
      "name": "cci_2m",
      "options": {
         "providerShortTag": "CCI"
      },
      "services": {
         "wms": {
            "url": "https://vortices.npm.ac.uk/thredds/wms/CCI_ALL-v2.0-MONTHLY?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://vortices.npm.ac.uk/thredds/wcs/CCI_ALL-v2.0-MONTHLY?",
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
            "niceName": "Chlorophyll-a Concentration",
            "interval": "Monthly",
            "indicator_type": [
               "Chlorophyll Indicators"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "chlor_a_bias": {
            "niceName": " Chlorophyll-a Concentration uncertainty",
            "interval": "Monthly",
            "indicator_type": [                                       
               "Chlorophyll Indicators"                                         
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"                                        
         },
         "chlor_a_rmsd": {
            "niceName": "Chlorophyll-a RMS uncertainty",
            "interval": "Monthly",
            "indicator_type": [ 
               "Chlorophyll Indicators" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "MODISA_nobs": {
            "niceName": "Count of the number of observations from the MODIS (Aqua)",
            "interval": "Monthly",
            "indicator_type": [ 
               "Count of Observations" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "MERIS_nobs": {
            "niceName": "Count of the number of observations from the MERIS sensor",
            "interval": "Monthly",
            "indicator_type": [ 
               "Count of Observations" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "SeaWiFS_nobs": {
            "niceName": "Count of the number of observations from the SeaWiFS sensor",
            "interval": "Monthly",
            "indicator_type": [ 
               "Count of Observations" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "total_nobs": {
            "niceName": "Count of the total number of observations",
            "interval": "Monthly",
            "indicator_type": [ 
               "Count of Observations" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "water_class1": {
            "niceName": "Water Class 1",
            "interval": "Monthly",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "water_class2": {
            "niceName": "Water Class 2",
            "interval": "Monthly",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "water_class3": {
            "niceName": "Water Class 3",
            "interval": "Monthly",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "water_class4": {
            "niceName": "Water Class 4",
            "interval": "Monthly",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "water_class5": {
            "niceName": "Water Class 5",
            "interval": "Monthly",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "water_class6": {
            "niceName": "Water Class 6",
            "interval": "Monthly",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "water_class7": {
            "niceName": "Water Class 7",
            "interval": "Monthly",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "water_class8": {
            "niceName": "Water Class 8",
            "interval": "Monthly",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "water_class9": {
            "niceName": "Water Class 9",
            "interval": "Monthly",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "water_class9": {
            "niceName": "Water Class 9",
            "interval": "Monthly",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "water_class10": {
            "niceName": "Water Class 10",
            "interval": "Monthly",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "water_class11": {
            "niceName": "Water Class 11",
            "interval": "Monthly",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "water_class12": {
            "niceName": "Water Class 12",
            "interval": "Monthly",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "water_class13": {
            "niceName": "Water Class 13",
            "interval": "Monthly",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "water_class14": {
            "niceName": "Water Class 14",
            "interval": "Monthly",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "aph_412": {
            "niceName": "Phytoplankton absorption coefficient",
            "wavelength": "412 nm",
            "interval": "Monthly",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "aph_443": {
            "niceName": "Phytoplankton absorption coefficient",
            "wavelength": "443 nm",
            "interval": "Monthly",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "aph_490": {
            "niceName": "Phytoplankton absorption coefficient",
            "wavelength": "490 nm",
            "interval": "Monthly",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "aph_510": {
            "niceName": "Phytoplankton absorption coefficient",
            "wavelength": "510 nm",
            "interval": "Monthly",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "aph_555": {
            "niceName": "Phytoplankton absorption coefficient",
            "wavelength": "555 nm",
            "interval": "Monthly",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "aph_670": {
            "niceName": "Phytoplankton absorption coefficient",
            "wavelength": "670 nm",
            "interval": "Monthly",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "atot_412": {
            "niceName": "Total absorption coefficient",
            "wavelength": "412 nm",
            "interval": "Monthly",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "atot_443": {
            "niceName": "Total absorption coefficient",
            "wavelength": "443 nm",
            "interval": "Monthly",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "atot_490": {
            "niceName": "Total absorption coefficient",
            "wavelength": "490 nm",
            "interval": "Monthly",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "atot_510": {
            "niceName": "Total absorption coefficient",
            "wavelength": "510 nm",
            "interval": "Monthly",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "atot_555": {
            "niceName": "Total absorption coefficient",
            "wavelength": "555 nm",
            "interval": "Monthly",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "atot_670": {
            "niceName": "Total absorption coefficient",
            "wavelength": "670 nm",
            "interval": "Monthly",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "adg_412": {
            "niceName": "Absorption coefficient for dissolved and detrital material",
            "wavelength": "412 nm",
            "interval": "Monthly",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "adg_443": {
            "niceName": "Absorption coefficient for dissolved and detrital material",
            "wavelength": "443 nm",
            "interval": "Monthly",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "adg_490": {
            "niceName": "Absorption coefficient for dissolved and detrital material",
            "wavelength": "490 nm",
            "interval": "Monthly",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "adg_510": {
            "niceName": "Absorption coefficient for dissolved and detrital material",
            "wavelength": "510 nm",
            "interval": "Monthly",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "adg_555": {
            "niceName": "Absorption coefficient for dissolved and detrital material",
            "wavelength": "555 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "cci_version": "Version 2.0"
         },
         "adg_670": {
            "niceName": "Absorption coefficient for dissolved and detrital material",
            "wavelength": "670 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "cci_version": "Version 2.0"
         },
         "bbp_412": {
            "niceName": "Particulate backscattering coefficient for dissolved and detrital material",
            "wavelength": "412 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "cci_version": "Version 2.0"
         },
         "bbp_443": {
            "niceName": "Particulate backscattering coefficient for dissolved and detrital material",
            "wavelength": "443 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "cci_version": "Version 2.0"
         },
         "bbp_490": {
            "niceName": "Particulate backscattering coefficient for dissolved and detrital material",
            "wavelength": "490 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "cci_version": "Version 2.0"
         },
         "bbp_510": {
            "niceName": "Particulate backscattering coefficient for dissolved and detrital material",
            "wavelength": "510 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "cci_version": "Version 2.0"
         },
         "bbp_555": {
            "niceName": "Particulate backscattering coefficient for dissolved and detrital material",
            "wavelength": "555 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "cci_version": "Version 2.0"
         },
         "bbp_670": {
            "niceName": "Particulate backscattering coefficient for dissolved and detrital material",
            "wavelength": "670 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "cci_version": "Version 2.0"
         },
         "Rrs_412": {
            "niceName": "Remote sensing reflectance",
            "wavelength": "412 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "cci_version": "Version 2.0"
         },
         "Rrs_443": {
            "niceName": "Remote sensing reflectance",
            "wavelength": "443 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "cci_version": "Version 2.0"
         },
         "Rrs_490": {
            "niceName": "Remote sensing reflectance",
            "wavelength": "490 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "cci_version": "Version 2.0"
         },
         "Rrs_510": {
            "niceName": "Remote sensing reflectance",
            "wavelength": "510 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "cci_version": "Version 2.0"
         },
         "Rrs_555": {
            "niceName": "Remote sensing reflectance",
            "wavelength": "555 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "cci_version": "Version 2.0"
         },
         "Rrs_670": {
            "niceName": "Remote sensing reflectance",
            "wavelength": "670 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "cci_version": "Version 2.0"
         },
         "kd_490": {
            "niceName": "Downwelling attenuation coefficient at 490nm",
            "interval": "Monthly",
            "indicator_type": [
               "Water Turbidity Indicators"
            ],
            "cci_version": "Version 2.0"
         },
         "aph_412_bias": {
            "niceName": "Phytoplankton absorption coefficient uncertainty",
            "wavelength": "412 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "cci_version": "Version 2.0"
         },
         "aph_443_bias": {
            "niceName": "Phytoplankton absorption coefficient uncertainty",
            "wavelength": "443 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "cci_version": "Version 2.0"
         },
         "aph_490_bias": {
            "niceName": "Phytoplankton absorption coefficient uncertainty",
            "wavelength": "490 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "cci_version": "Version 2.0"
         },
         "aph_510_bias": {
            "niceName": "Phytoplankton absorption coefficient uncertainty",
            "wavelength": "510 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "cci_version": "Version 2.0"
         },
         "aph_555_bias": {
            "niceName": "Phytoplankton absorption coefficient uncertainty",
            "wavelength": "555 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "cci_version": "Version 2.0"
         },
         "aph_670_bias": {
            "niceName": "Phytoplankton absorption coefficient uncertainty",
            "wavelength": "670 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "cci_version": "Version 2.0"
         },
         "adg_412_bias": {
            "niceName": "Absorption coefficient for dissolved and detrital material uncertainty",
            "wavelength": "412 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "cci_version": "Version 2.0"
         },
         "adg_443_bias": {
            "niceName": "Absorption coefficient for dissolved and detrital material uncertainty",
            "wavelength": "443 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "cci_version": "Version 2.0"
         },
         "adg_490_bias": {
            "niceName": "Absorption coefficient for dissolved and detrital material uncertainty",
            "wavelength": "490 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "cci_version": "Version 2.0"
         },
         "adg_510_bias": {
            "niceName": "Absorption coefficient for dissolved and detrital material uncertainty",
            "wavelength": "510 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "cci_version": "Version 2.0"
         },
         "adg_555_bias": {
            "niceName": "Absorption coefficient for dissolved and detrital material uncertainty",
            "wavelength": "555 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "cci_version": "Version 2.0"
         },
         "adg_670_bias": {
            "niceName": "Absorption coefficient for dissolved and detrital material uncertainty",
            "wavelength": "670 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "cci_version": "Version 2.0"
         },
         "Rrs_412_bias": {
            "niceName": "Remote sensing reflectance uncertainty",
            "wavelength": "412 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "cci_version": "Version 2.0"
         },
         "Rrs_443_bias": {
            "niceName": "Remote sensing reflectance uncertainty",
            "wavelength": "443 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "cci_version": "Version 2.0"
         },
         "Rrs_490_bias": {
            "niceName": "Remote sensing reflectance uncertainty",
            "wavelength": "490 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "cci_version": "Version 2.0"
         },
         "Rrs_510_bias": {
            "niceName": "Remote sensing reflectance uncertainty",
            "wavelength": "510 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "cci_version": "Version 2.0"
         },
         "Rrs_555_bias": {
            "niceName": "Remote sensing reflectance uncertainty",
            "wavelength": "555 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "cci_version": "Version 2.0"
         },
         "Rrs_670_bias": {
            "niceName": "Remote sensing reflectance uncertainty",
            "wavelength": "670 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "cci_version": "Version 2.0"
         },
         "kd_490_bias": {
            "niceName": "Downwelling attenuation coefficient at 490nm uncertainty",
            "interval": "Monthly",
            "indicator_type": [
               "Water Turbidity Indicators"
            ],
            "cci_version": "Version 2.0"
         },
         "aph_412_rmsd": {
            "niceName": "Phytoplankton absorption coefficient RMS uncertainty",
            "wavelength": "412 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "cci_version": "Version 2.0"
         },
         "aph_443_rmsd": {
            "niceName": "Phytoplankton absorption coefficient RMS uncertainty",
            "wavelength": "443 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "cci_version": "Version 2.0"
         },
         "aph_490_rmsd": {
            "niceName": "Phytoplankton absorption coefficient RMS uncertainty",
            "wavelength": "490 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "cci_version": "Version 2.0"
         },
         "aph_510_rmsd": {
            "niceName": "Phytoplankton absorption coefficient RMS uncertainty",
            "wavelength": "510 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "cci_version": "Version 2.0"
         },
         "aph_555_rmsd": {
            "niceName": "Phytoplankton absorption coefficient RMS uncertainty",
            "wavelength": "555 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "cci_version": "Version 2.0"
         },
         "aph_670_rmsd": {
            "niceName": "Phytoplankton absorption coefficient RMS uncertainty",
            "wavelength": "670 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "cci_version": "Version 2.0"
         },
         "adg_412_rmsd": {
            "niceName": "Absorption coefficient for dissolved and detrital material RMS uncertainty",
            "wavelength": "412 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "cci_version": "Version 2.0"
         },
         "adg_443_rmsd": {
            "niceName": "Absorption coefficient for dissolved and detrital material RMS uncertainty",
            "wavelength": "443 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "cci_version": "Version 2.0"
         },
         "adg_490_rmsd": {
            "niceName": "Absorption coefficient for dissolved and detrital material RMS uncertainty",
            "wavelength": "490 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "cci_version": "Version 2.0"
         },
         "adg_510_rmsd": {
            "niceName": "Absorption coefficient for dissolved and detrital material RMS uncertainty",
            "wavelength": "510 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "cci_version": "Version 2.0"
         },
         "adg_555_rmsd": {
            "niceName": "Absorption coefficient for dissolved and detrital material RMS uncertainty",
            "wavelength": "555 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "cci_version": "Version 2.0"
         },
         "adg_670_rmsd": {
            "niceName": "Absorption coefficient for dissolved and detrital material RMS uncertainty",
            "wavelength": "670 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "cci_version": "Version 2.0"
         },
         "Rrs_412_rmsd": {
            "niceName": "Remote sensing reflectance RMS uncertainty",
            "wavelength": "412 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "cci_version": "Version 2.0"
         },
         "Rrs_443_rmsd": {
            "niceName": "Remote sensing reflectance RMS uncertainty",
            "wavelength": "443 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "cci_version": "Version 2.0"
         },
         "Rrs_490_rmsd": {
            "niceName": "Remote sensing reflectance RMS uncertainty",
            "wavelength": "490 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "cci_version": "Version 2.0"
         },
         "Rrs_510_rmsd": {
            "niceName": "Remote sensing reflectance RMS uncertainty",
            "wavelength": "510 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "cci_version": "Version 2.0"
         },
         "Rrs_555_rmsd": {
            "niceName": "Remote sensing reflectance RMS uncertainty",
            "wavelength": "555 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "cci_version": "Version 2.0"
         },
         "Rrs_670_rmsd": {
            "niceName": "Remote sensing reflectance RMS uncertainty",
            "wavelength": "670 nm",
            "interval": "Monthly",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "cci_version": "Version 2.0"
         },
         "kd_490_rmsd": {
            "niceName": "Downwelling attenuation coefficient at 490nm RMS uncertainty",
            "interval": "Monthly",
            "indicator_type": [
               "Water Turbidity Indicators"
            ],
            "cci_version": "Version 2.0"
         },

      }
   },
   {
      "name": "cci_2d",
      "options": {
         "providerShortTag": "CCI"
      },
      "services": {
         "wms": {
            "url": "https://vortices.npm.ac.uk/thredds/wms/CCI_ALL-v2.0-DAILY?",
            "params": {
               "GetCapabilities": {
                  "SERVICE": "WMS",
                  "request": "GetCapabilities",
                  "version": "1.3.0"
               }
            }
         },
         "wcs": {
            "url": "https://vortices.npm.ac.uk/thredds/wcs/CCI_ALL-v2.0-DAILY?",
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
            "niceName": "Chlorophyll-a Concentration",
            "interval": "Daily",
            "indicator_type": [
               "Chlorophyll Indicators"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "chlor_a_bias": {
            "niceName": " Chlorophyll-a Concentration uncertainty",
            "interval": "Daily",
            "indicator_type": [                                       
               "Chlorophyll Indicators"                                         
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"                                        
         },
         "chlor_a_rmsd": {
            "niceName": "Chlorophyll-a RMS uncertainty",
            "interval": "Daily",
            "indicator_type": [ 
               "Chlorophyll Indicators" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "MODISA_nobs": {
            "niceName": "Count of the number of observations from the MODIS (Aqua)",
            "interval": "Daily",
            "indicator_type": [ 
               "Count of Observations" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "MERIS_nobs": {
            "niceName": "Count of the number of observations from the MERIS sensor",
            "interval": "Daily",
            "indicator_type": [ 
               "Count of Observations" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "SeaWiFS_nobs": {
            "niceName": "Count of the number of observations from the SeaWiFS sensor",
            "interval": "Daily",
            "indicator_type": [ 
               "Count of Observations" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "total_nobs": {
            "niceName": "Count of the total number of observations",
            "interval": "Daily",
            "indicator_type": [ 
               "Count of Observations" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "water_class1": {
            "niceName": "Water Class 1",
            "interval": "Daily",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "water_class2": {
            "niceName": "Water Class 2",
            "interval": "Daily",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "water_class3": {
            "niceName": "Water Class 3",
            "interval": "Daily",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "water_class4": {
            "niceName": "Water Class 4",
            "interval": "Daily",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "water_class5": {
            "niceName": "Water Class 5",
            "interval": "Daily",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "water_class6": {
            "niceName": "Water Class 6",
            "interval": "Daily",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "water_class7": {
            "niceName": "Water Class 7",
            "interval": "Daily",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "water_class8": {
            "niceName": "Water Class 8",
            "interval": "Daily",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "water_class9": {
            "niceName": "Water Class 9",
            "interval": "Daily",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "water_class10": {
            "niceName": "Water Class 10",
            "interval": "Monthly",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "water_class11": {
            "niceName": "Water Class 11",
            "interval": "Monthly",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "water_class12": {
            "niceName": "Water Class 12",
            "interval": "Monthly",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "water_class13": {
            "niceName": "Water Class 13",
            "interval": "Monthly",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "water_class14": {
            "niceName": "Water Class 14",
            "interval": "Monthly",
            "indicator_type": [ 
               "Water Class" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "aph_412": {
            "niceName": "Phytoplankton absorption coefficient",
            "wavelength": "412 nm",
            "interval": "Daily",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "aph_443": {
            "niceName": "Phytoplankton absorption coefficient",
            "wavelength": "443 nm",
            "interval": "Daily",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "aph_490": {
            "niceName": "Phytoplankton absorption coefficient",
            "wavelength": "490 nm",
            "interval": "Daily",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "aph_510": {
            "niceName": "Phytoplankton absorption coefficient",
            "wavelength": "510 nm",
            "interval": "Daily",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "aph_555": {
            "niceName": "Phytoplankton absorption coefficient",
            "wavelength": "555 nm",
            "interval": "Daily",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "aph_670": {
            "niceName": "Phytoplankton absorption coefficient",
            "wavelength": "670 nm",
            "interval": "Daily",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "atot_412": {
            "niceName": "Total absorption coefficient",
            "wavelength": "412 nm",
            "interval": "Daily",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "atot_443": {
            "niceName": "Total absorption coefficient",
            "wavelength": "443 nm",
            "interval": "Daily",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "atot_490": {
            "niceName": "Total absorption coefficient",
            "wavelength": "490 nm",
            "interval": "Daily",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "atot_510": {
            "niceName": "Total absorption coefficient",
            "wavelength": "510 nm",
            "interval": "Daily",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "atot_555": {
            "niceName": "Total absorption coefficient",
            "wavelength": "555 nm",
            "interval": "Daily",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "atot_670": {
            "niceName": "Total absorption coefficient",
            "wavelength": "670 nm",
            "interval": "Daily",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "adg_412": {
            "niceName": "Absorption coefficient for dissolved and detrital material",
            "wavelength": "412 nm",
            "interval": "Daily",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "adg_443": {
            "niceName": "Absorption coefficient for dissolved and detrital material",
            "wavelength": "443 nm",
            "interval": "Daily",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "adg_490": {
            "niceName": "Absorption coefficient for dissolved and detrital material",
            "wavelength": "490 nm",
            "interval": "Daily",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "adg_510": {
            "niceName": "Absorption coefficient for dissolved and detrital material",
            "wavelength": "510 nm",
            "interval": "Daily",
            "indicator_type": [ 
               "Inherent Optical Properties" 
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0" 
         },
         "adg_555": {
            "niceName": "Absorption coefficient for dissolved and detrital material",
            "wavelength": "555 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "adg_670": {
            "niceName": "Absorption coefficient for dissolved and detrital material",
            "wavelength": "670 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "bbp_412": {
            "niceName": "Particulate backscattering coefficient for dissolved and detrital material",
            "wavelength": "412 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "bbp_443": {
            "niceName": "Particulate backscattering coefficient for dissolved and detrital material",
            "wavelength": "443 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "bbp_490": {
            "niceName": "Particulate backscattering coefficient for dissolved and detrital material",
            "wavelength": "490 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "bbp_510": {
            "niceName": "Particulate backscattering coefficient for dissolved and detrital material",
            "wavelength": "510 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "bbp_555": {
            "niceName": "Particulate backscattering coefficient for dissolved and detrital material",
            "wavelength": "555 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "bbp_670": {
            "niceName": "Particulate backscattering coefficient for dissolved and detrital material",
            "wavelength": "670 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "Rrs_412": {
            "niceName": "Remote sensing reflectance",
            "wavelength": "412 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "Rrs_443": {
            "niceName": "Remote sensing reflectance",
            "wavelength": "443 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "Rrs_490": {
            "niceName": "Remote sensing reflectance",
            "wavelength": "490 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "Rrs_510": {
            "niceName": "Remote sensing reflectance",
            "wavelength": "510 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "Rrs_555": {
            "niceName": "Remote sensing reflectance",
            "wavelength": "555 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "Rrs_670": {
            "niceName": "Remote sensing reflectance",
            "wavelength": "670 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "kd_490": {
            "niceName": "Downwelling attenuation coefficient at 490nm",
            "interval": "Daily",
            "indicator_type": [
               "Water Turbidity Indicators"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "aph_412_bias": {
            "niceName": "Phytoplankton absorption coefficient uncertainty",
            "wavelength": "412 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "aph_443_bias": {
            "niceName": "Phytoplankton absorption coefficient uncertainty",
            "wavelength": "443 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "aph_490_bias": {
            "niceName": "Phytoplankton absorption coefficient uncertainty",
            "wavelength": "490 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "aph_510_bias": {
            "niceName": "Phytoplankton absorption coefficient uncertainty",
            "wavelength": "510 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "aph_555_bias": {
            "niceName": "Phytoplankton absorption coefficient uncertainty",
            "wavelength": "555 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "aph_670_bias": {
            "niceName": "Phytoplankton absorption coefficient uncertainty",
            "wavelength": "670 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "adg_412_bias": {
            "niceName": "Absorption coefficient for dissolved and detrital material uncertainty",
            "wavelength": "412 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "adg_443_bias": {
            "niceName": "Absorption coefficient for dissolved and detrital material uncertainty",
            "wavelength": "443 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "adg_490_bias": {
            "niceName": "Absorption coefficient for dissolved and detrital material uncertainty",
            "wavelength": "490 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "adg_510_bias": {
            "niceName": "Absorption coefficient for dissolved and detrital material uncertainty",
            "wavelength": "510 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "adg_555_bias": {
            "niceName": "Absorption coefficient for dissolved and detrital material uncertainty",
            "wavelength": "555 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "adg_670_bias": {
            "niceName": "Absorption coefficient for dissolved and detrital material uncertainty",
            "wavelength": "670 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "Rrs_412_bias": {
            "niceName": "Remote sensing reflectance uncertainty",
            "wavelength": "412 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "Rrs_443_bias": {
            "niceName": "Remote sensing reflectance uncertainty",
            "wavelength": "443 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "Rrs_490_bias": {
            "niceName": "Remote sensing reflectance uncertainty",
            "wavelength": "490 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "Rrs_510_bias": {
            "niceName": "Remote sensing reflectance uncertainty",
            "wavelength": "510 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "Rrs_555_bias": {
            "niceName": "Remote sensing reflectance uncertainty",
            "wavelength": "555 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "Rrs_670_bias": {
            "niceName": "Remote sensing reflectance uncertainty",
            "wavelength": "670 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "kd_490_bias": {
            "niceName": "Downwelling attenuation coefficient at 490nm uncertainty",
            "interval": "Daily",
            "indicator_type": [
               "Water Turbidity Indicators"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "aph_412_rmsd": {
            "niceName": "Phytoplankton absorption coefficient RMS uncertainty",
            "wavelength": "412 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "aph_443_rmsd": {
            "niceName": "Phytoplankton absorption coefficient RMS uncertainty",
            "wavelength": "443 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "aph_490_rmsd": {
            "niceName": "Phytoplankton absorption coefficient RMS uncertainty",
            "wavelength": "490 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "aph_510_rmsd": {
            "niceName": "Phytoplankton absorption coefficient RMS uncertainty",
            "wavelength": "510 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "aph_555_rmsd": {
            "niceName": "Phytoplankton absorption coefficient RMS uncertainty",
            "wavelength": "555 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "aph_670_rmsd": {
            "niceName": "Phytoplankton absorption coefficient RMS uncertainty",
            "wavelength": "670 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "adg_412_rmsd": {
            "niceName": "Absorption coefficient for dissolved and detrital material RMS uncertainty",
            "wavelength": "412 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "adg_443_rmsd": {
            "niceName": "Absorption coefficient for dissolved and detrital material RMS uncertainty",
            "wavelength": "443 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "adg_490_rmsd": {
            "niceName": "Absorption coefficient for dissolved and detrital material RMS uncertainty",
            "wavelength": "490 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "adg_510_rmsd": {
            "niceName": "Absorption coefficient for dissolved and detrital material RMS uncertainty",
            "wavelength": "510 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "adg_555_rmsd": {
            "niceName": "Absorption coefficient for dissolved and detrital material RMS uncertainty",
            "wavelength": "555 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "adg_670_rmsd": {
            "niceName": "Absorption coefficient for dissolved and detrital material RMS uncertainty",
            "wavelength": "670 nm",
            "interval": "Daily",
            "indicator_type": [
               "Inherent Optical Properties"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "Rrs_412_rmsd": {
            "niceName": "Remote sensing reflectance RMS uncertainty",
            "wavelength": "412 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "Rrs_443_rmsd": {
            "niceName": "Remote sensing reflectance RMS uncertainty",
            "wavelength": "443 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "Rrs_490_rmsd": {
            "niceName": "Remote sensing reflectance RMS uncertainty",
            "wavelength": "490 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "Rrs_510_rmsd": {
            "niceName": "Remote sensing reflectance RMS uncertainty",
            "wavelength": "510 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "Rrs_555_rmsd": {
            "niceName": "Remote sensing reflectance RMS uncertainty",
            "wavelength": "555 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "Rrs_670_rmsd": {
            "niceName": "Remote sensing reflectance RMS uncertainty",
            "wavelength": "670 nm",
            "interval": "Daily",
            "indicator_type": [
               "Sea Surface Reflectance and Characterisation"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },
         "kd_490_rmsd": {
            "niceName": "Downwelling attenuation coefficient at 490nm RMS uncertainty",
            "interval": "Daily",
            "indicator_type": [
               "Water Turbidity Indicators"
            ],
            "data_provider": "ESA",
            "cci_version": "Version 2.0"
         },

      }
   }
]