/*------------------------------------*\
   Configuration
   This file is for the configuration
   of the GIS Portal.

   browseCategories - Used to define
   which categories to be shown in the
   browse panel. This is currently
   limited to 2.
\*------------------------------------*/



gisportal.config = {
   siteMode: "production", //(development|production)
   browseCategories : {
      "indicator_type" : "Indicators",
      "region": "Region",
      "data_provider" : "Provider"
   },
   paths: {
    graphServer: 'http://localhost:8112/',
    middlewarePath: '/service'
   },

   // Should layers auto scale by default
   autoScale: true,
   // set the default map
   defaultBaseMap: 'EOX',

   // Should layers auto scale by default
   autoScale: true,

   requiresTermsAndCondictions: true,

};

