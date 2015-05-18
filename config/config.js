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
      "wavelength": "Wavelength",
      "interval": "Interval",
      "cci_version": "CCI Version",
   },
   browseMode : 'selectlist',                       // (tabs|selectlist) tabs (default) = original method of 3 tabs; selectlist = makes all available categories selectable from a drop down list
   defaultCategory: '',                     // only used when browseMode = selectlist; any key value from browseCategories
         
   paths: {
    graphServer: 'https://www.oceancolour.org/plotting/',
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

