HIT_URL = 'https://www.pfizer.com/science/drug-product-pipeline'
CRAWL_URL = 'https://www.pfizer.com/views/ajax'

IPAYLOAD = "field_ugcf_therapeutic_area%5B%5D=70491&field_ugcf_therapeutic_area%5B%5D=14221&field_ugcf_therapeutic_area%5B%5D=71516&field_ugcf_therapeutic_area%5B%5D=14186&field_ugcf_therapeutic_area%5B%5D=14211&field_ugcf_therapeutic_area%5B%5D=14226&field_ugcf_therapeutic_area%5B%5D=14151&field_ugcf_phase_of_development%5B%5D=Registration&field_ugcf_phase_of_development%5B%5D=Phase+3&field_ugcf_phase_of_development%5B%5D=Phase+2&field_ugcf_phase_of_development%5B%5D=Phase+1&field_ugcf_submission_type%5B%5D=14241&field_ugcf_submission_type%5B%5D=14161&field_ugcf_submission_type%5B%5D=14196&field_ugcf_compound_type%5B%5D=14191&field_ugcf_compound_type%5B%5D=14236&field_ugcf_compound_type%5B%5D=14176&field_ugcf_compound_type%5B%5D=14156&search_api_aggregation_1=&discontinued=0&view_name=product_pipeline_page&view_display_id=pane_global&view_args=&view_path=node%2F322516&view_base_path=product-pipeline-page&view_dom_id=0cbba8c77519c5b6bca53b9fb4bb9366&pager_element=0&ajax_html_ids=pfizercom-header%2Cblock-menu-menu-menu-header-additional-2016%2Cblock-menu-menu-c%2Chealth-professionals%2Cconnect-with-us%2Cblock-block-8%2Csearchbox_012390703595722449228%3Artvx5nj8aua%2Cblock-tb-megamenu-menu-menu-header-2016%2Ctb-megamenu-column-20%2Ctb-megamenu-column-19%2Ctb-megamenu-column-22%2Ctb-megamenu-column-21%2Ctb-megamenu-column-25%2Ctb-megamenu-column-23%2Ctb-megamenu-column-24%2Cblock-views-64f4696f0c85ee570de2a6ac0a1a6850%2Ctb-megamenu-column-28%2Ctb-megamenu-column-26%2Ctb-megamenu-column-27%2Ctb-megamenu-column-31%2Ctb-megamenu-column-29%2Ctb-megamenu-column-30%2Ctb-megamenu-column-33%2Ctb-megamenu-column-32%2Cblock-views-8875090b99647b983af48dae47b85843%2Ctb-megamenu-column-35%2Ctb-megamenu-column-34%2Ctb-megamenu-column-38%2Ctb-megamenu-column-36%2Ctb-megamenu-column-37%2Ctb-megamenu-column-40%2Ctb-megamenu-column-39%2Cblock-views-1cf750f217df7b90cc1a5a7c763b442d%2Ctb-megamenu-column-44%2Ctb-megamenu-column-41%2Ctb-megamenu-column-42%2Ctb-megamenu-column-43%2Ctb-megamenu-column-48%2Ctb-megamenu-column-45%2Ctb-megamenu-column-46%2Ctb-megamenu-column-47%2Ctb-megamenu-column-51%2Ctb-megamenu-column-49%2Cblock-views-b487901db6b49f9cc1021c9686250e9b%2Ctb-megamenu-column-50%2Ctb-megamenu-column-54%2Ctb-megamenu-column-52%2Ctb-megamenu-column-53%2Ctb-megamenu-column-56%2Ctb-megamenu-column-55%2Ctb-megamenu-column-58%2Ctb-megamenu-column-57%2Cblock-views-25e2a08784cc10bdd2a484485e1a39ca%2Cblock-menu-menu-menu-header-additional-2016%2Cmobile-divider%2Cblock-pfe-pfizercom-banner-top-banner%2Cgl-base%2Chtml-blocks-wrapper%2Chtml-blocks-wrapper%2Chtml-blocks-wrapper%2Cblock-panels-mini-mini-product-pipeline-global%2Cmini-panel-mini_product_pipeline_global%2Cquicktabs-quicktabs_pipeline_global%2Cquicktabs-tab-quicktabs_pipeline_global-0%2Cquicktabs-tab-quicktabs_pipeline_global-1%2Cquicktabs-container-quicktabs_pipeline_global%2Cquicktabs-tabpage-quicktabs_pipeline_global-0%2Cviews-exposed-form-product-pipeline-page-pane-global%2Cedit-field-ugcf-therapeutic-area-wrapper%2Cedit-field-ugcf-therapeutic-area-70491%2Cedit-field-ugcf-therapeutic-area-14221%2Cedit-field-ugcf-therapeutic-area-71516%2Cedit-field-ugcf-therapeutic-area-14186%2Cedit-field-ugcf-therapeutic-area-14211%2Cedit-field-ugcf-therapeutic-area-14226%2Cedit-field-ugcf-therapeutic-area-14151%2Cedit-field-ugcf-phase-of-development-wrapper%2Cedit-field-ugcf-phase-of-development-registration%2Cedit-field-ugcf-phase-of-development-phase-3%2Cedit-field-ugcf-phase-of-development-phase-2%2Cedit-field-ugcf-phase-of-development-phase-1%2Cedit-field-ugcf-submission-type-wrapper%2Cedit-field-ugcf-submission-type-14241%2Cedit-field-ugcf-submission-type-14161%2Cedit-field-ugcf-submission-type-14196%2Cedit-field-ugcf-compound-type-wrapper%2Cedit-field-ugcf-compound-type-14191%2Cedit-field-ugcf-compound-type-14236%2Cedit-field-ugcf-compound-type-14176%2Cedit-field-ugcf-compound-type-14156%2Cedit-search-api-aggregation-1-wrapper%2Cedit-search-api-aggregation-1%2Cedit-submit-product-pipeline-page%2Cquicktabs-tabpage-quicktabs_pipeline_global-1%2Cpfizercom-footer%2Cblock-tb-megamenu-menu-menu-footer-2016%2Ctb-megamenu-column-2%2Ctb-megamenu-column-1%2Ctb-megamenu-column-4%2Ctb-megamenu-column-3%2Ctb-megamenu-column-6%2Ctb-megamenu-column-5%2Ctb-megamenu-column-8%2Ctb-megamenu-column-7%2Ctb-megamenu-column-10%2Ctb-megamenu-column-9%2Cblock-tb-megamenu-menu-menu-footer-additional-2016%2Ctb-megamenu-column-12%2Ctb-megamenu-column-11%2Ctb-megamenu-column-14%2Ctb-megamenu-column-13%2Ctb-megamenu-column-16%2Ctb-megamenu-column-15%2Ctb-megamenu-column-18%2Ctb-megamenu-column-17%2Cblock-block-636%2Cblock-block-198%2Cfancybox-tmp%2Cfancybox-loading%2Cfancybox-overlay%2Cfancybox-wrap%2Cfancybox-outer%2Cfancybox-bg-n%2Cfancybox-bg-ne%2Cfancybox-bg-e%2Cfancybox-bg-se%2Cfancybox-bg-s%2Cfancybox-bg-sw%2Cfancybox-bg-w%2Cfancybox-bg-nw%2Cfancybox-content%2Cfancybox-close%2Cfancybox-title%2Cfancybox-left%2Cfancybox-left-ico%2Cfancybox-right%2Cfancybox-right-ico&ajax_page_state%5Btheme%5D=pfizer_com_zen&ajax_page_state%5Btheme_token%5D=kRrJYNRZ6QNVg9wQpZG3r7PHLqiSG9iw0iSwPWXV7K0&ajax_page_state%5Bcss%5D%5Bmodules%2Fsystem%2Fsystem.base.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fsystem%2Fsystem.menus.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fsystem%2Fsystem.messages.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fsystem%2Fsystem.theme.css%5D=1&ajax_page_state%5Bcss%5D%5Bmisc%2Fui%2Fjquery.ui.core.css%5D=1&ajax_page_state%5Bcss%5D%5Bmisc%2Fui%2Fjquery.ui.theme.css%5D=1&ajax_page_state%5Bcss%5D%5Bmisc%2Fui%2Fjquery.ui.menu.css%5D=1&ajax_page_state%5Bcss%5D%5Bmisc%2Fui%2Fjquery.ui.autocomplete.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fcomment%2Fcomment.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fdate%2Fdate_api%2Fdate.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fdate%2Fdate_popup%2Fthemes%2Fdatepicker.1.7.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Ffield%2Ftheme%2Ffield.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fnode%2Fnode.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fpoll%2Fpoll.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fsearch%2Fsearch.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fuser%2Fuser.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fmodules%2Fcontrib%2Fyoutube%2Fcss%2Fyoutube.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fextlink%2Fextlink.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fviews%2Fcss%2Fviews.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fckeditor%2Fcss%2Fckeditor.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fmodules%2Fcontrib%2Fapachesolr_autocomplete%2Fapachesolr_autocomplete.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fctools%2Fcss%2Fctools.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fmodules%2Fcontrib%2Fnice_menus%2Fnice_menus.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fmodules%2Fcontrib%2Fnice_menus%2Fnice_menus_default.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fpanels%2Fcss%2Fpanels.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Flibraries%2Fslick%2Fslick%2Fslick.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Flibraries%2Fslick%2Fslick%2Fslick-theme.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Flibraries%2Fsuperfish%2Fcss%2Fsuperfish.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Flibraries%2Fsuperfish%2Fcss%2Fsuperfish-vertical.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Flibraries%2Fsuperfish%2Fcss%2Fsuperfish-navbar.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fmodules%2Fcustom%2Fpfizer_settings%2Fcss%2Fckeditor-custom.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fmodules%2Ffeatures%2Fpfe_pfizercom_landings%2Fplugins%2Flayouts%2Fgl_base%2Fgl_base.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Ffield_collection%2Ffield_collection.theme.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fpanels%2Fplugins%2Flayouts%2Fflexible%2Fflexible.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fmodules%2Fcontrib%2Fquicktabs%2Fcss%2Fquicktabs.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fmodules%2Fcontrib%2Fquicktabs%2Fquicktabs_tabstyles%2Ftabstyles%2Fsky%2Fsky.css%5D=1&ajax_page_state%5Bcss%5D%5Bpublic%3A%2F%2Fctools%2Fcss%2F49cab732d3baa84c89b8adaa2e7faac6.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com%2Fcss%2Faddthis.css%5D=1&ajax_page_state%5Bcss%5D%5Bhttps%3A%2F%2Fcdnjs.cloudflare.com%2Fajax%2Flibs%2Ffont-awesome%2F4.4.0%2Fcss%2Ffont-awesome.min.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fmodules%2Fupdated%2Ftb_megamenu%2Fcss%2Fbootstrap.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fmodules%2Fupdated%2Ftb_megamenu%2Fcss%2Fbase.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fmodules%2Fupdated%2Ftb_megamenu%2Fcss%2Fdefault.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fmodules%2Fupdated%2Ftb_megamenu%2Fcss%2Fcompatibility.css%5D=1&ajax_page_state%5Bcss%5D%5Bhttps%3A%2F%2Fs3-eu-west-1.amazonaws.com%2Fsfactorycorp%2Fv3.1redesign%2FProd%2FMaster%2Fcss%2Fterritory.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fmodules%2Fupdated%2Ftb_megamenu%2Fcss%2Fstyles%2Fblack.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Flibraries%2Ffancybox%2Ffancybox.css%5D=1&ajax_page_state%5Bcss%5D%5Bpublic%3A%2F%2Fctools%2Fcss%2Fd41d8cd98f00b204e9800998ecf8427e.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fsystem.base.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fsystem.menus.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fsystem.messages.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fsystem.theme.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fcomment.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fnode.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fcss%2Ffont-awesome.min.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fcss%2Fmagnific-popup.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fjs%2Fvendor%2Fslick%2Fslick.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fjs%2Fvendor%2Fmagnific-popup%2Fmagnific-popup.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fcss%2Fstyles.css%5D=1&ajax_page_state%5Bjs%5D%5B%2F%2Fcode.jquery.com%2Fjquery-1.7.2.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fjquery.once.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fdrupal.js%5D=1&ajax_page_state%5Bjs%5D%5B%2F%2Fcode.jquery.com%2Fui%2F1.10.2%2Fjquery-ui.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fjquery_update%2Freplace%2Fui%2Fexternal%2Fjquery.cookie.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fjquery_update%2Freplace%2Fmisc%2Fjquery.form.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Flibraries%2Ffancybox%2Ffancybox.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fajax.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fjquery_update%2Fjs%2Fjquery_update.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fupdated%2Ffb_instant_articles%2Fmodules%2Ffb_instant_articles_display%2Fjs%2Fadmin.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Ffeatures%2Fpfe_pfizercom_content_types%2Fpfe_distributors%2Fjs%2Fpfe_distributors.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fcustom%2Fpfizer_msds%2Fjs%2Fpfizer_msds.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fcustom%2Fpfizer_menu%2Fjs%2Fpfizer_menu.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fextlink%2Fextlink.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fprogress.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fcontrib%2Fapachesolr_autocomplete%2Fapachesolr_autocomplete_jqueryui.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fcontrib%2Fnice_menus%2Fsuperfish%2Fjs%2Fsuperfish.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fcontrib%2Fnice_menus%2Fsuperfish%2Fjs%2Fjquery.bgiframe.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fcontrib%2Fnice_menus%2Fsuperfish%2Fjs%2Fjquery.hoverIntent.minified.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fcontrib%2Fnice_menus%2Fnice_menus.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Flibraries%2Fslick%2Fslick%2Fslick.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Flibraries%2Fsuperfish%2Fjquery.hoverIntent.minified.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Flibraries%2Fsuperfish%2Fjquery.bgiframe.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Flibraries%2Fsuperfish%2Fsuperfish.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Flibraries%2Fsuperfish%2Fsupersubs.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Flibraries%2Fsuperfish%2Fsupposition.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Flibraries%2Fsuperfish%2Fsftouchscreen.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fcustom%2Fpfizer_settings%2Fjs%2Fpfizer_settings.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fcustom%2Fpfizer_settings%2Fjs%2Fa_button_fix.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fviews%2Fjs%2Fbase.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fbetter_exposed_filters%2Fbetter_exposed_filters.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fctools%2Fjs%2Fauto-submit.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fcustom%2Fpipeline_search%2Fpipeline_search.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fupdated%2Fviews_load_more%2Fviews_load_more.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fviews%2Fjs%2Fajax_view.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fcontrib%2Fquicktabs%2Fjs%2Fquicktabs.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fupdated%2Ftb_megamenu%2Fjs%2Ftb-megamenu-frontend.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fupdated%2Ftb_megamenu%2Fjs%2Ftb-megamenu-touch.js%5D=1&ajax_page_state%5Bjs%5D%5Bhttps%3A%2F%2Fs3-eu-west-1.amazonaws.com%2Fsfactorycorp%2Fv3.1redesign%2FProd%2FMaster%2Fjs%2Fterritory_selector_config.js%5D=1&ajax_page_state%5Bjs%5D%5Bhttps%3A%2F%2Fs3-eu-west-1.amazonaws.com%2Fsfactorycorp%2Fv3.1redesign%2FProd%2FMaster%2Fjs%2Fterritory_selector.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fcustom%2Ffeatured_story_settings%2Fjs%2Ffeatured-story-detail.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fjs%2Fextended-page.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fcustom%2Fpfizer_omniture_integration%2Fjs%2Fpfizer_omniture_integration.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fcustom%2Fpfizer_omniture_integration%2Fjs%2Fpfizer_omniture_integration_video.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fcustom%2Fpfizer_omniture_integration%2Fjs%2Fpfizer_omniture_integration_matrix.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fjs%2Fvendor%2Fmagnific-popup%2Fjquery.magnific-popup.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fjs%2Fscript.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fjs%2Fglobal.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fjs%2Fheader.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fjs%2Fvendor%2Fjquery-throttle-debounce%2Fjquery.ba-throttle-debounce.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fjs%2Fvendor%2Fslick%2Fslick.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fjs%2Fvendor%2Fmagnific-popup%2Fjquery.magnific-popup.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fjs%2Fparagraph.js%5D=1&ajax_page_state%5Bjquery_version%5D=1.7"

PAYLOAD = "view_name=product_pipeline_page&view_display_id=pane_global&view_args=&view_path=node%2F322516&view_base_path=product-pipeline-page&view_dom_id=fcae955a752c0cbf8941c0d2acb1ccc4&pager_element=0&field_ugcf_therapeutic_area%5B0%5D=70491&field_ugcf_therapeutic_area%5B1%5D=14221&field_ugcf_therapeutic_area%5B2%5D=71516&field_ugcf_therapeutic_area%5B3%5D=14186&field_ugcf_therapeutic_area%5B4%5D=14211&field_ugcf_therapeutic_area%5B5%5D=14226&field_ugcf_therapeutic_area%5B6%5D=14151&field_ugcf_phase_of_development%5B0%5D=Registration&field_ugcf_phase_of_development%5B1%5D=Phase+3&field_ugcf_phase_of_development%5B2%5D=Phase+2&field_ugcf_phase_of_development%5B3%5D=Phase+1&field_ugcf_submission_type%5B0%5D=14241&field_ugcf_submission_type%5B1%5D=14161&field_ugcf_submission_type%5B2%5D=14196&field_ugcf_compound_type%5B0%5D=14191&field_ugcf_compound_type%5B1%5D=14236&field_ugcf_compound_type%5B2%5D=14176&field_ugcf_compound_type%5B3%5D=14156&discontinued=0&page={0}&ajax_html_ids=www-widgetapi-script%2Cpfizercom-header%2Cblock-menu-menu-menu-header-additional-2016%2Cblock-menu-menu-c%2Chealth-professionals%2Cconnect-with-us%2Cblock-block-8%2Csearchbox_012390703595722449228%3Artvx5nj8aua%2Cblock-tb-megamenu-menu-menu-header-2016%2Ctb-megamenu-column-20%2Ctb-megamenu-column-19%2Ctb-megamenu-column-22%2Ctb-megamenu-column-21%2Ctb-megamenu-column-25%2Ctb-megamenu-column-23%2Ctb-megamenu-column-24%2Cblock-views-64f4696f0c85ee570de2a6ac0a1a6850%2Ctb-megamenu-column-28%2Ctb-megamenu-column-26%2Ctb-megamenu-column-27%2Ctb-megamenu-column-31%2Ctb-megamenu-column-29%2Ctb-megamenu-column-30%2Ctb-megamenu-column-33%2Ctb-megamenu-column-32%2Cblock-views-8875090b99647b983af48dae47b85843%2Ctb-megamenu-column-35%2Ctb-megamenu-column-34%2Ctb-megamenu-column-38%2Ctb-megamenu-column-36%2Ctb-megamenu-column-37%2Ctb-megamenu-column-40%2Ctb-megamenu-column-39%2Cblock-views-1cf750f217df7b90cc1a5a7c763b442d%2Ctb-megamenu-column-44%2Ctb-megamenu-column-41%2Ctb-megamenu-column-42%2Ctb-megamenu-column-43%2Ctb-megamenu-column-48%2Ctb-megamenu-column-45%2Ctb-megamenu-column-46%2Ctb-megamenu-column-47%2Ctb-megamenu-column-51%2Ctb-megamenu-column-49%2Cblock-views-b487901db6b49f9cc1021c9686250e9b%2Ctb-megamenu-column-50%2Ctb-megamenu-column-54%2Ctb-megamenu-column-52%2Ctb-megamenu-column-53%2Ctb-megamenu-column-56%2Ctb-megamenu-column-55%2Ctb-megamenu-column-58%2Ctb-megamenu-column-57%2Cblock-views-25e2a08784cc10bdd2a484485e1a39ca%2Cblock-menu-menu-menu-header-additional-2016%2Cmobile-divider%2Cblock-pfe-pfizercom-banner-top-banner%2Cgl-base%2Chtml-blocks-wrapper%2Chtml-blocks-wrapper%2Chtml-blocks-wrapper%2Cblock-panels-mini-mini-product-pipeline-global%2Cmini-panel-mini_product_pipeline_global%2Cquicktabs-quicktabs_pipeline_global%2Cquicktabs-tab-quicktabs_pipeline_global-0%2Cquicktabs-tab-quicktabs_pipeline_global-1%2Cquicktabs-container-quicktabs_pipeline_global%2Cquicktabs-tabpage-quicktabs_pipeline_global-0%2Cviews-exposed-form-product-pipeline-page-pane-global%2Cedit-field-ugcf-therapeutic-area-wrapper%2Cedit-field-ugcf-therapeutic-area-70491%2Cedit-field-ugcf-therapeutic-area-14221%2Cedit-field-ugcf-therapeutic-area-71516%2Cedit-field-ugcf-therapeutic-area-14186%2Cedit-field-ugcf-therapeutic-area-14211%2Cedit-field-ugcf-therapeutic-area-14226%2Cedit-field-ugcf-therapeutic-area-14151%2Cedit-field-ugcf-phase-of-development-wrapper%2Cedit-field-ugcf-phase-of-development-registration%2Cedit-field-ugcf-phase-of-development-phase-3%2Cedit-field-ugcf-phase-of-development-phase-2%2Cedit-field-ugcf-phase-of-development-phase-1%2Cedit-field-ugcf-submission-type-wrapper%2Cedit-field-ugcf-submission-type-14241%2Cedit-field-ugcf-submission-type-14161%2Cedit-field-ugcf-submission-type-14196%2Cedit-field-ugcf-compound-type-wrapper%2Cedit-field-ugcf-compound-type-14191%2Cedit-field-ugcf-compound-type-14236%2Cedit-field-ugcf-compound-type-14176%2Cedit-field-ugcf-compound-type-14156%2Cedit-search-api-aggregation-1-wrapper%2Cedit-search-api-aggregation-1%2Cedit-submit-product-pipeline-page%2Cquicktabs-tabpage-quicktabs_pipeline_global-1%2Catstbx%2Cat-3fe831d1-8337-4d2a-aead-270df3ac269d%2Cat-svg-facebook-1%2Cat-svg-twitter-2%2Cat-svg-linkedin-3%2Cat-svg-google_plusone_share-4%2Cat-svg-email-5%2Cat-svg-print-6%2Cpfizercom-footer%2Cblock-tb-megamenu-menu-menu-footer-2016%2Ctb-megamenu-column-2%2Ctb-megamenu-column-1%2Ctb-megamenu-column-4%2Ctb-megamenu-column-3%2Ctb-megamenu-column-6%2Ctb-megamenu-column-5%2Ctb-megamenu-column-8%2Ctb-megamenu-column-7%2Ctb-megamenu-column-10%2Ctb-megamenu-column-9%2Cblock-tb-megamenu-menu-menu-footer-additional-2016%2Ctb-megamenu-column-12%2Ctb-megamenu-column-11%2Ctb-megamenu-column-14%2Ctb-megamenu-column-13%2Ctb-megamenu-column-16%2Ctb-megamenu-column-15%2Ctb-megamenu-column-18%2Ctb-megamenu-column-17%2Cblock-block-636%2Cblock-block-198%2C_atssh%2C_atssh236%2Cservice-icons-0%2Cfancybox-tmp%2Cfancybox-loading%2Cfancybox-overlay%2Cfancybox-wrap%2Cfancybox-outer%2Cfancybox-bg-n%2Cfancybox-bg-ne%2Cfancybox-bg-e%2Cfancybox-bg-se%2Cfancybox-bg-s%2Cfancybox-bg-sw%2Cfancybox-bg-w%2Cfancybox-bg-nw%2Cfancybox-content%2Cfancybox-close%2Cfancybox-title%2Cfancybox-left%2Cfancybox-left-ico%2Cfancybox-right%2Cfancybox-right-ico&ajax_page_state%5Btheme%5D=pfizer_com_zen&ajax_page_state%5Btheme_token%5D=4rwNXlBZgEue5lUMJFYowGjifz6zwt_TjgNlQSoQmSI&ajax_page_state%5Bcss%5D%5Bmodules%2Fsystem%2Fsystem.base.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fsystem%2Fsystem.menus.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fsystem%2Fsystem.messages.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fsystem%2Fsystem.theme.css%5D=1&ajax_page_state%5Bcss%5D%5Bmisc%2Fui%2Fjquery.ui.core.css%5D=1&ajax_page_state%5Bcss%5D%5Bmisc%2Fui%2Fjquery.ui.theme.css%5D=1&ajax_page_state%5Bcss%5D%5Bmisc%2Fui%2Fjquery.ui.menu.css%5D=1&ajax_page_state%5Bcss%5D%5Bmisc%2Fui%2Fjquery.ui.autocomplete.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fcomment%2Fcomment.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fdate%2Fdate_api%2Fdate.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fdate%2Fdate_popup%2Fthemes%2Fdatepicker.1.7.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Ffield%2Ftheme%2Ffield.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fnode%2Fnode.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fpoll%2Fpoll.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fsearch%2Fsearch.css%5D=1&ajax_page_state%5Bcss%5D%5Bmodules%2Fuser%2Fuser.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fmodules%2Fcontrib%2Fyoutube%2Fcss%2Fyoutube.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fextlink%2Fextlink.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fviews%2Fcss%2Fviews.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fckeditor%2Fcss%2Fckeditor.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fmodules%2Fcontrib%2Fapachesolr_autocomplete%2Fapachesolr_autocomplete.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fctools%2Fcss%2Fctools.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fmodules%2Fcontrib%2Fnice_menus%2Fnice_menus.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fmodules%2Fcontrib%2Fnice_menus%2Fnice_menus_default.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fpanels%2Fcss%2Fpanels.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Flibraries%2Fslick%2Fslick%2Fslick.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Flibraries%2Fslick%2Fslick%2Fslick-theme.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Flibraries%2Fsuperfish%2Fcss%2Fsuperfish.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Flibraries%2Fsuperfish%2Fcss%2Fsuperfish-vertical.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Flibraries%2Fsuperfish%2Fcss%2Fsuperfish-navbar.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fmodules%2Fcustom%2Fpfizer_settings%2Fcss%2Fckeditor-custom.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fmodules%2Ffeatures%2Fpfe_pfizercom_landings%2Fplugins%2Flayouts%2Fgl_base%2Fgl_base.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Ffield_collection%2Ffield_collection.theme.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fpanels%2Fplugins%2Flayouts%2Fflexible%2Fflexible.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fmodules%2Fcontrib%2Fquicktabs%2Fcss%2Fquicktabs.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fmodules%2Fcontrib%2Fquicktabs%2Fquicktabs_tabstyles%2Ftabstyles%2Fsky%2Fsky.css%5D=1&ajax_page_state%5Bcss%5D%5Bpublic%3A%2F%2Fctools%2Fcss%2F49cab732d3baa84c89b8adaa2e7faac6.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com%2Fcss%2Faddthis.css%5D=1&ajax_page_state%5Bcss%5D%5Bhttps%3A%2F%2Fcdnjs.cloudflare.com%2Fajax%2Flibs%2Ffont-awesome%2F4.4.0%2Fcss%2Ffont-awesome.min.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fmodules%2Fupdated%2Ftb_megamenu%2Fcss%2Fbootstrap.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fmodules%2Fupdated%2Ftb_megamenu%2Fcss%2Fbase.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fmodules%2Fupdated%2Ftb_megamenu%2Fcss%2Fdefault.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fmodules%2Fupdated%2Ftb_megamenu%2Fcss%2Fcompatibility.css%5D=1&ajax_page_state%5Bcss%5D%5Bhttps%3A%2F%2Fs3-eu-west-1.amazonaws.com%2Fsfactorycorp%2Fv3.1redesign%2FProd%2FMaster%2Fcss%2Fterritory.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fmodules%2Fupdated%2Ftb_megamenu%2Fcss%2Fstyles%2Fblack.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Flibraries%2Ffancybox%2Ffancybox.css%5D=1&ajax_page_state%5Bcss%5D%5Bpublic%3A%2F%2Fctools%2Fcss%2Fd41d8cd98f00b204e9800998ecf8427e.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fsystem.base.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fsystem.menus.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fsystem.messages.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fsystem.theme.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fcomment.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fnode.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fcss%2Ffont-awesome.min.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fcss%2Fmagnific-popup.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fjs%2Fvendor%2Fslick%2Fslick.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fjs%2Fvendor%2Fmagnific-popup%2Fmagnific-popup.css%5D=1&ajax_page_state%5Bcss%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fcss%2Fstyles.css%5D=1&ajax_page_state%5Bjs%5D%5B%2F%2Fcode.jquery.com%2Fjquery-1.7.2.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fjquery.once.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fdrupal.js%5D=1&ajax_page_state%5Bjs%5D%5B%2F%2Fcode.jquery.com%2Fui%2F1.10.2%2Fjquery-ui.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fjquery_update%2Freplace%2Fui%2Fexternal%2Fjquery.cookie.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fjquery_update%2Freplace%2Fmisc%2Fjquery.form.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Flibraries%2Ffancybox%2Ffancybox.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fajax.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fjquery_update%2Fjs%2Fjquery_update.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fupdated%2Ffb_instant_articles%2Fmodules%2Ffb_instant_articles_display%2Fjs%2Fadmin.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Ffeatures%2Fpfe_pfizercom_content_types%2Fpfe_distributors%2Fjs%2Fpfe_distributors.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fcustom%2Fpfizer_msds%2Fjs%2Fpfizer_msds.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fcustom%2Fpfizer_menu%2Fjs%2Fpfizer_menu.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fextlink%2Fextlink.js%5D=1&ajax_page_state%5Bjs%5D%5Bmisc%2Fprogress.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fcontrib%2Fapachesolr_autocomplete%2Fapachesolr_autocomplete_jqueryui.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fcontrib%2Fnice_menus%2Fsuperfish%2Fjs%2Fsuperfish.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fcontrib%2Fnice_menus%2Fsuperfish%2Fjs%2Fjquery.bgiframe.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fcontrib%2Fnice_menus%2Fsuperfish%2Fjs%2Fjquery.hoverIntent.minified.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fcontrib%2Fnice_menus%2Fnice_menus.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Flibraries%2Fslick%2Fslick%2Fslick.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Flibraries%2Fsuperfish%2Fjquery.hoverIntent.minified.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Flibraries%2Fsuperfish%2Fjquery.bgiframe.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Flibraries%2Fsuperfish%2Fsuperfish.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Flibraries%2Fsuperfish%2Fsupersubs.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Flibraries%2Fsuperfish%2Fsupposition.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Flibraries%2Fsuperfish%2Fsftouchscreen.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fcustom%2Fpfizer_settings%2Fjs%2Fpfizer_settings.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fcustom%2Fpfizer_settings%2Fjs%2Fa_button_fix.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fviews%2Fjs%2Fbase.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fbetter_exposed_filters%2Fbetter_exposed_filters.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fctools%2Fjs%2Fauto-submit.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fcustom%2Fpipeline_search%2Fpipeline_search.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fupdated%2Fviews_load_more%2Fviews_load_more.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fall%2Fmodules%2Fcontrib%2Fviews%2Fjs%2Fajax_view.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fcontrib%2Fquicktabs%2Fjs%2Fquicktabs.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fupdated%2Ftb_megamenu%2Fjs%2Ftb-megamenu-frontend.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fupdated%2Ftb_megamenu%2Fjs%2Ftb-megamenu-touch.js%5D=1&ajax_page_state%5Bjs%5D%5Bhttps%3A%2F%2Fs3-eu-west-1.amazonaws.com%2Fsfactorycorp%2Fv3.1redesign%2FProd%2FMaster%2Fjs%2Fterritory_selector_config.js%5D=1&ajax_page_state%5Bjs%5D%5Bhttps%3A%2F%2Fs3-eu-west-1.amazonaws.com%2Fsfactorycorp%2Fv3.1redesign%2FProd%2FMaster%2Fjs%2Fterritory_selector.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fcustom%2Ffeatured_story_settings%2Fjs%2Ffeatured-story-detail.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fjs%2Fextended-page.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fcustom%2Fpfizer_omniture_integration%2Fjs%2Fpfizer_omniture_integration.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fcustom%2Fpfizer_omniture_integration%2Fjs%2Fpfizer_omniture_integration_video.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fmodules%2Fcustom%2Fpfizer_omniture_integration%2Fjs%2Fpfizer_omniture_integration_matrix.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fjs%2Fvendor%2Fmagnific-popup%2Fjquery.magnific-popup.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fjs%2Fscript.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fjs%2Fglobal.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fjs%2Fheader.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fjs%2Fvendor%2Fjquery-throttle-debounce%2Fjquery.ba-throttle-debounce.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fjs%2Fvendor%2Fslick%2Fslick.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fjs%2Fvendor%2Fmagnific-popup%2Fjquery.magnific-popup.min.js%5D=1&ajax_page_state%5Bjs%5D%5Bsites%2Fdefault%2Fthemes%2Fpfizer_com_zen%2Fjs%2Fparagraph.js%5D=1&ajax_page_state%5Bjquery_version%5D=1.7"

HEADERS = {
    'accept': "application/json, text/javascript, */*; q=0.01",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.9",
    'Cache-Control': "no-cache",
    'content-length': "16131",
    'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
    'cookie': "__cfduid=d73934ed2f6da524e32c73d6acff694291538024131; __utmz=254873161.1538024139.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __ncuid=6d9bdf50-1445-421a-bb33-46ace483eaa1; s_fid=5DA188AEF3700235-2C6666EBF4734B5D; _ga=GA1.2.731980972.1538024139; has_js=1; _gid=GA1.2.709237720.1538127342; __utma=254873161.731980972.1538024139.1538024139.1538127342.2; __utmc=254873161; __utmt=1; s_ppn=www.pfizer.com%3Escience%3Edrug-product-pipeline; prevPage=www.pfizer.com%3Escience%3Edrug-product-pipeline; s_cc=true; _gat_ncAudienceInsightsGa=1; __atuvc=4%7C39; __atuvs=5badf5ee442fef1b001; __utmb=254873161.3.10.1538127342; s_sess=%20s_ppvl%3Dwww.pfizer.com%25253Escience%25253Edrug-product-pipeline%252C31%252C31%252C1724%252C1920%252C978%252C1920%252C1080%252C1%252CP%3B%20s_ppv%3Dwww.pfizer.com%25253Escience%25253Edrug-product-pipeline%252C29%252C29%252C1724%252C1920%252C978%252C1920%252C1080%252C1%252CP%3B; s_nr=1538127400291-Repeat",
    'origin': "https://www.pfizer.com",
    'pragma': "no-cache",
    'referer': "https://www.pfizer.com/science/drug-product-pipeline",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    'x-newrelic-id': "VgYEU15QGwEIUlRQBQY=",
    'x-requested-with': "XMLHttpRequest"
}

# Maximum loading page to crawl
MAX_LOOP_PAGE = 2