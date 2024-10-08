import datetime

from pixiv_utils.pixiv_crawler import (
    BookmarkCrawler,
    KeywordCrawler,
    RankingCrawler,
    UserCrawler,
    checkDir,
    displayAllConfig,
    download_config,
    network_config,
    ranking_config,
    user_config,
)

import random

high_artist = ["38297201","69101980","15231158","13539582"]

def downloadRanking():
    """
    Download artworks from rankings

    NOTE: Require cookie for R18 images!

    Args:
        capacity (int): flow capacity, default is 1024MB
    """
    network_config.proxy["https"] = "127.0.0.1:7890"
    user_config.user_id = "user_jvey4484"
    user_config.cookie = "first_visit_datetime_pc=2024-09-21%2012%3A00%3A13; p_ab_id=2; p_ab_id_2=5; p_ab_d_id=1425353051; yuid_b=JJZmIYg; __utmc=235335808; device_token=931550d568f055adcf880fae1b9b9853; c_type=19; privacy_policy_notification=0; a_type=0; b_type=1; _im_vid=01J898CAPK2YX76S6EF910S32K; __gads=ID=c686e1054b1e97a0:T=1726887662:RT=1726887662:S=ALNI_Mah3n8iSkQm7TrRmJ2WiPhYLVtrhg; __gpi=UID=00000f12b3e37e81:T=1726887662:RT=1726887662:S=ALNI_MZ4NdsCvf3V7k4W0dx2sM4L1GNn-Q; __eoi=ID=967af6e011995033:T=1726887662:RT=1726887662:S=AA-AfjYYccT-Ev8YkpYoXBl6Mrni; __cf_bm=d0Pf.m1H07nDA_CREmcJBcNLlgmoGwpF5l2gZ25ib58-1727058269-1.0.1.1-wT1_n4TOL.sIglcM1_xxPvJvFBL5qocuo2MB3AJ0uWVIIXYmXb4SSgQlnejF7CBLdwXWggK38UY7dBDaT9Y.BRKghqAzEqLjrgIG7m4pVsA; __utma=235335808.1668812789.1726887616.1726887616.1727058270.2; __utmz=235335808.1727058270.2.2.utmcsr=bing|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; cf_clearance=fg8upL4Rklvf0juE0fz6OjJhQamRM2kfuiTT51b0nIg-1727058270-1.2.1.1-v3EfJorQo83A0hrV6zHexnI95z2VV.mS8PNrrv0YsYxVKM_NHRq85NkYTLSMJzU50Nk5E16G9ZAL_ezisjdMTncwj4skgBwRZuoFcIElFUn_lPEuvZ_.W4Mi8MR6IzUikVS7Zdc1zFjD8ZO9Xbr2CIVsniphe39lhZM6FV0kOzzKQtAV._dWu8qWk1pyl_W70lJ1g94g8yX2FvfZ8tq4jmDp51o4_VfFx_8TNOWYAxNVr48VcWtUeflpKq7zBwx4tLXYPJEAgrBaLmmdBG.1yqwDloUL80NpvFBB7.7ngtHci1nfDHKU3.ZrQ5yA3.LC9Nd6Hj_vxbLXF7wUz78JxdromdpLJXv_5S6zXScsfnU_.3cgw2B_5KtfZDchHB4Sq78_DCxS_aVuqOMfwyBfXw; _gid=GA1.2.1820646992.1727058272; PHPSESSID=103712710_UuOw0AAwB1tnYrgr55AJJ5XKgzl27bTn; _ga_MZ1NL4PHH0=GS1.1.1727058284.1.1.1727058358.0.0.0; FCNEC=%5B%5B%22AKsRol_XfV0fHydVC5mhR_rRjOocO7ISCLSqeEABmVoDsd37DHStjgTTG40DiUEPIWJcVS8roG_LHRJBk0bcxsxOoBRbDnBE_NFOCId6OyNe_dhgzyGwD_IgxgHBSA01ladMP7BNcTVJgSWzdRQjglT-JNg_L9-G6g%3D%3D%22%5D%5D; privacy_policy_agreement=7; _im_uid.3929=b.adf1a323bfe1d6af; login_ever=yes; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=103712710=1^9=p_ab_id=2=1^10=p_ab_id_2=5=1^11=lang=zh=1; __utmb=235335808.5.10.1727058270; _ga_75BBYNYN9J=GS1.1.1727058271.2.1.1727058723.0.0.0; _ga=GA1.2.1668812789.1726887616"

    download_config.with_tag = False
    ranking_config.start_date = datetime.date(2024, 5, 1)
    ranking_config.range = 2
    ranking_config.mode = "weekly"
    ranking_config.content_mode = "illust"
    ranking_config.num_artwork = 20

    displayAllConfig()
    checkDir(download_config.store_path)

    app = RankingCrawler(capacity=200)
    app.run()

def downloadRanking():
    """
    Download artworks from rankings

    NOTE: Require cookie for R18 images!

    Args:
        capacity (int): flow capacity, default is 1024MB
    """
    network_config.proxy["https"] = "127.0.0.1:7890"
    user_config.user_id = "user_jvey4484"
    user_config.cookie = "first_visit_datetime_pc=2024-09-21%2012%3A00%3A13; p_ab_id=2; p_ab_id_2=5; p_ab_d_id=1425353051; yuid_b=JJZmIYg; __utmc=235335808; device_token=931550d568f055adcf880fae1b9b9853; c_type=19; privacy_policy_notification=0; a_type=0; b_type=1; _im_vid=01J898CAPK2YX76S6EF910S32K; __gads=ID=c686e1054b1e97a0:T=1726887662:RT=1726887662:S=ALNI_Mah3n8iSkQm7TrRmJ2WiPhYLVtrhg; __gpi=UID=00000f12b3e37e81:T=1726887662:RT=1726887662:S=ALNI_MZ4NdsCvf3V7k4W0dx2sM4L1GNn-Q; __eoi=ID=967af6e011995033:T=1726887662:RT=1726887662:S=AA-AfjYYccT-Ev8YkpYoXBl6Mrni; __cf_bm=d0Pf.m1H07nDA_CREmcJBcNLlgmoGwpF5l2gZ25ib58-1727058269-1.0.1.1-wT1_n4TOL.sIglcM1_xxPvJvFBL5qocuo2MB3AJ0uWVIIXYmXb4SSgQlnejF7CBLdwXWggK38UY7dBDaT9Y.BRKghqAzEqLjrgIG7m4pVsA; __utma=235335808.1668812789.1726887616.1726887616.1727058270.2; __utmz=235335808.1727058270.2.2.utmcsr=bing|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; cf_clearance=fg8upL4Rklvf0juE0fz6OjJhQamRM2kfuiTT51b0nIg-1727058270-1.2.1.1-v3EfJorQo83A0hrV6zHexnI95z2VV.mS8PNrrv0YsYxVKM_NHRq85NkYTLSMJzU50Nk5E16G9ZAL_ezisjdMTncwj4skgBwRZuoFcIElFUn_lPEuvZ_.W4Mi8MR6IzUikVS7Zdc1zFjD8ZO9Xbr2CIVsniphe39lhZM6FV0kOzzKQtAV._dWu8qWk1pyl_W70lJ1g94g8yX2FvfZ8tq4jmDp51o4_VfFx_8TNOWYAxNVr48VcWtUeflpKq7zBwx4tLXYPJEAgrBaLmmdBG.1yqwDloUL80NpvFBB7.7ngtHci1nfDHKU3.ZrQ5yA3.LC9Nd6Hj_vxbLXF7wUz78JxdromdpLJXv_5S6zXScsfnU_.3cgw2B_5KtfZDchHB4Sq78_DCxS_aVuqOMfwyBfXw; _gid=GA1.2.1820646992.1727058272; PHPSESSID=103712710_UuOw0AAwB1tnYrgr55AJJ5XKgzl27bTn; _ga_MZ1NL4PHH0=GS1.1.1727058284.1.1.1727058358.0.0.0; FCNEC=%5B%5B%22AKsRol_XfV0fHydVC5mhR_rRjOocO7ISCLSqeEABmVoDsd37DHStjgTTG40DiUEPIWJcVS8roG_LHRJBk0bcxsxOoBRbDnBE_NFOCId6OyNe_dhgzyGwD_IgxgHBSA01ladMP7BNcTVJgSWzdRQjglT-JNg_L9-G6g%3D%3D%22%5D%5D; privacy_policy_agreement=7; _im_uid.3929=b.adf1a323bfe1d6af; login_ever=yes; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=103712710=1^9=p_ab_id=2=1^10=p_ab_id_2=5=1^11=lang=zh=1; __utmb=235335808.5.10.1727058270; _ga_75BBYNYN9J=GS1.1.1727058271.2.1.1727058723.0.0.0; _ga=GA1.2.1668812789.1726887616"

    download_config.with_tag = False
    ranking_config.start_date = datetime.date(2024, 9, 1)
    ranking_config.range = 7
    ranking_config.mode = "weekly"
    ranking_config.content_mode = "illust"
    ranking_config.num_artwork = 20

    displayAllConfig()
    checkDir(download_config.store_path)

    app = RankingCrawler(capacity=200)
    image_ids = app.collect_urls()
    ids = []
    for id in image_ids:
        ids.append(f"https://pixiv.cat/{id}.png")
    return ids

def downloadRanking_urls_r18():
    """
    Download artworks from rankings

    NOTE: Require cookie for R18 images!

    Args:
        capacity (int): flow capacity, default is 1024MB
    """
    network_config.proxy["https"] = "127.0.0.1:7890"
    user_config.user_id = "user_jvey4484"
    user_config.cookie = "first_visit_datetime_pc=2024-09-21%2012%3A00%3A13; p_ab_id=2; p_ab_id_2=5; p_ab_d_id=1425353051; yuid_b=JJZmIYg; __utmc=235335808; device_token=931550d568f055adcf880fae1b9b9853; c_type=19; privacy_policy_notification=0; a_type=0; b_type=1; _im_vid=01J898CAPK2YX76S6EF910S32K; __gads=ID=c686e1054b1e97a0:T=1726887662:RT=1726887662:S=ALNI_Mah3n8iSkQm7TrRmJ2WiPhYLVtrhg; __gpi=UID=00000f12b3e37e81:T=1726887662:RT=1726887662:S=ALNI_MZ4NdsCvf3V7k4W0dx2sM4L1GNn-Q; __eoi=ID=967af6e011995033:T=1726887662:RT=1726887662:S=AA-AfjYYccT-Ev8YkpYoXBl6Mrni; __cf_bm=d0Pf.m1H07nDA_CREmcJBcNLlgmoGwpF5l2gZ25ib58-1727058269-1.0.1.1-wT1_n4TOL.sIglcM1_xxPvJvFBL5qocuo2MB3AJ0uWVIIXYmXb4SSgQlnejF7CBLdwXWggK38UY7dBDaT9Y.BRKghqAzEqLjrgIG7m4pVsA; __utma=235335808.1668812789.1726887616.1726887616.1727058270.2; __utmz=235335808.1727058270.2.2.utmcsr=bing|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; cf_clearance=fg8upL4Rklvf0juE0fz6OjJhQamRM2kfuiTT51b0nIg-1727058270-1.2.1.1-v3EfJorQo83A0hrV6zHexnI95z2VV.mS8PNrrv0YsYxVKM_NHRq85NkYTLSMJzU50Nk5E16G9ZAL_ezisjdMTncwj4skgBwRZuoFcIElFUn_lPEuvZ_.W4Mi8MR6IzUikVS7Zdc1zFjD8ZO9Xbr2CIVsniphe39lhZM6FV0kOzzKQtAV._dWu8qWk1pyl_W70lJ1g94g8yX2FvfZ8tq4jmDp51o4_VfFx_8TNOWYAxNVr48VcWtUeflpKq7zBwx4tLXYPJEAgrBaLmmdBG.1yqwDloUL80NpvFBB7.7ngtHci1nfDHKU3.ZrQ5yA3.LC9Nd6Hj_vxbLXF7wUz78JxdromdpLJXv_5S6zXScsfnU_.3cgw2B_5KtfZDchHB4Sq78_DCxS_aVuqOMfwyBfXw; _gid=GA1.2.1820646992.1727058272; PHPSESSID=103712710_UuOw0AAwB1tnYrgr55AJJ5XKgzl27bTn; _ga_MZ1NL4PHH0=GS1.1.1727058284.1.1.1727058358.0.0.0; FCNEC=%5B%5B%22AKsRol_XfV0fHydVC5mhR_rRjOocO7ISCLSqeEABmVoDsd37DHStjgTTG40DiUEPIWJcVS8roG_LHRJBk0bcxsxOoBRbDnBE_NFOCId6OyNe_dhgzyGwD_IgxgHBSA01ladMP7BNcTVJgSWzdRQjglT-JNg_L9-G6g%3D%3D%22%5D%5D; privacy_policy_agreement=7; _im_uid.3929=b.adf1a323bfe1d6af; login_ever=yes; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=103712710=1^9=p_ab_id=2=1^10=p_ab_id_2=5=1^11=lang=zh=1; __utmb=235335808.5.10.1727058270; _ga_75BBYNYN9J=GS1.1.1727058271.2.1.1727058723.0.0.0; _ga=GA1.2.1668812789.1726887616"

    download_config.with_tag = False
    ranking_config.start_date = datetime.date(2024, 5, 1)
    ranking_config.range = 2
    ranking_config.mode = "weekly_r18"
    ranking_config.content_mode = "illust"
    ranking_config.num_artwork = 20

    displayAllConfig()
    checkDir(download_config.store_path)

    app = RankingCrawler(capacity=200)
    image_ids = app.collect_urls()
    ids = []
    for id in image_ids:
        ids.append(f"https://pixiv.cat/{id}.png")
    return ids
def downloadBookmark():
    """
    Download artworks from bookmark

    NOTE: Require cookie!

    Args:
        n_images (int): max download number, default is 200
        capacity (int): flow capacity, default is 1024MB
    """
    download_config.with_tag = False
    network_config.proxy["https"] = "127.0.0.1:7890"
    user_config.user_id = "user_jvey4484"
    user_config.cookie = "first_visit_datetime_pc=2024-09-21%2012%3A00%3A13; p_ab_id=2; p_ab_id_2=5; p_ab_d_id=1425353051; yuid_b=JJZmIYg; __utmc=235335808; device_token=931550d568f055adcf880fae1b9b9853; c_type=19; privacy_policy_notification=0; a_type=0; b_type=1; _im_vid=01J898CAPK2YX76S6EF910S32K; __gads=ID=c686e1054b1e97a0:T=1726887662:RT=1726887662:S=ALNI_Mah3n8iSkQm7TrRmJ2WiPhYLVtrhg; __gpi=UID=00000f12b3e37e81:T=1726887662:RT=1726887662:S=ALNI_MZ4NdsCvf3V7k4W0dx2sM4L1GNn-Q; __eoi=ID=967af6e011995033:T=1726887662:RT=1726887662:S=AA-AfjYYccT-Ev8YkpYoXBl6Mrni; __cf_bm=d0Pf.m1H07nDA_CREmcJBcNLlgmoGwpF5l2gZ25ib58-1727058269-1.0.1.1-wT1_n4TOL.sIglcM1_xxPvJvFBL5qocuo2MB3AJ0uWVIIXYmXb4SSgQlnejF7CBLdwXWggK38UY7dBDaT9Y.BRKghqAzEqLjrgIG7m4pVsA; __utma=235335808.1668812789.1726887616.1726887616.1727058270.2; __utmz=235335808.1727058270.2.2.utmcsr=bing|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; cf_clearance=fg8upL4Rklvf0juE0fz6OjJhQamRM2kfuiTT51b0nIg-1727058270-1.2.1.1-v3EfJorQo83A0hrV6zHexnI95z2VV.mS8PNrrv0YsYxVKM_NHRq85NkYTLSMJzU50Nk5E16G9ZAL_ezisjdMTncwj4skgBwRZuoFcIElFUn_lPEuvZ_.W4Mi8MR6IzUikVS7Zdc1zFjD8ZO9Xbr2CIVsniphe39lhZM6FV0kOzzKQtAV._dWu8qWk1pyl_W70lJ1g94g8yX2FvfZ8tq4jmDp51o4_VfFx_8TNOWYAxNVr48VcWtUeflpKq7zBwx4tLXYPJEAgrBaLmmdBG.1yqwDloUL80NpvFBB7.7ngtHci1nfDHKU3.ZrQ5yA3.LC9Nd6Hj_vxbLXF7wUz78JxdromdpLJXv_5S6zXScsfnU_.3cgw2B_5KtfZDchHB4Sq78_DCxS_aVuqOMfwyBfXw; _gid=GA1.2.1820646992.1727058272; PHPSESSID=103712710_UuOw0AAwB1tnYrgr55AJJ5XKgzl27bTn; _ga_MZ1NL4PHH0=GS1.1.1727058284.1.1.1727058358.0.0.0; FCNEC=%5B%5B%22AKsRol_XfV0fHydVC5mhR_rRjOocO7ISCLSqeEABmVoDsd37DHStjgTTG40DiUEPIWJcVS8roG_LHRJBk0bcxsxOoBRbDnBE_NFOCId6OyNe_dhgzyGwD_IgxgHBSA01ladMP7BNcTVJgSWzdRQjglT-JNg_L9-G6g%3D%3D%22%5D%5D; privacy_policy_agreement=7; _im_uid.3929=b.adf1a323bfe1d6af; login_ever=yes; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=103712710=1^9=p_ab_id=2=1^10=p_ab_id_2=5=1^11=lang=zh=1; __utmb=235335808.5.10.1727058270; _ga_75BBYNYN9J=GS1.1.1727058271.2.1.1727058723.0.0.0; _ga=GA1.2.1668812789.1726887616"

    displayAllConfig()
    checkDir(download_config.store_path)

    app = BookmarkCrawler(n_images=20, capacity=200)
    app.run()


def downloadUser_urls():
    """
    Download artworks from a single artist

    NOTE: Require cookie for R18 images!

    Args:
        artist_id (str): artist id
        capacity (int): flow capacity, default is 1024MB
    """
    network_config.proxy["https"] = "127.0.0.1:7890"
    user_config.user_id = "user_jvey4484"
    user_config.cookie = "first_visit_datetime_pc=2024-09-21%2012%3A00%3A13; p_ab_id=2; p_ab_id_2=5; p_ab_d_id=1425353051; yuid_b=JJZmIYg; __utmc=235335808; device_token=931550d568f055adcf880fae1b9b9853; c_type=19; privacy_policy_notification=0; a_type=0; b_type=1; _im_vid=01J898CAPK2YX76S6EF910S32K; __gads=ID=c686e1054b1e97a0:T=1726887662:RT=1726887662:S=ALNI_Mah3n8iSkQm7TrRmJ2WiPhYLVtrhg; __gpi=UID=00000f12b3e37e81:T=1726887662:RT=1726887662:S=ALNI_MZ4NdsCvf3V7k4W0dx2sM4L1GNn-Q; __eoi=ID=967af6e011995033:T=1726887662:RT=1726887662:S=AA-AfjYYccT-Ev8YkpYoXBl6Mrni; __cf_bm=d0Pf.m1H07nDA_CREmcJBcNLlgmoGwpF5l2gZ25ib58-1727058269-1.0.1.1-wT1_n4TOL.sIglcM1_xxPvJvFBL5qocuo2MB3AJ0uWVIIXYmXb4SSgQlnejF7CBLdwXWggK38UY7dBDaT9Y.BRKghqAzEqLjrgIG7m4pVsA; __utma=235335808.1668812789.1726887616.1726887616.1727058270.2; __utmz=235335808.1727058270.2.2.utmcsr=bing|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; cf_clearance=fg8upL4Rklvf0juE0fz6OjJhQamRM2kfuiTT51b0nIg-1727058270-1.2.1.1-v3EfJorQo83A0hrV6zHexnI95z2VV.mS8PNrrv0YsYxVKM_NHRq85NkYTLSMJzU50Nk5E16G9ZAL_ezisjdMTncwj4skgBwRZuoFcIElFUn_lPEuvZ_.W4Mi8MR6IzUikVS7Zdc1zFjD8ZO9Xbr2CIVsniphe39lhZM6FV0kOzzKQtAV._dWu8qWk1pyl_W70lJ1g94g8yX2FvfZ8tq4jmDp51o4_VfFx_8TNOWYAxNVr48VcWtUeflpKq7zBwx4tLXYPJEAgrBaLmmdBG.1yqwDloUL80NpvFBB7.7ngtHci1nfDHKU3.ZrQ5yA3.LC9Nd6Hj_vxbLXF7wUz78JxdromdpLJXv_5S6zXScsfnU_.3cgw2B_5KtfZDchHB4Sq78_DCxS_aVuqOMfwyBfXw; _gid=GA1.2.1820646992.1727058272; PHPSESSID=103712710_UuOw0AAwB1tnYrgr55AJJ5XKgzl27bTn; _ga_MZ1NL4PHH0=GS1.1.1727058284.1.1.1727058358.0.0.0; FCNEC=%5B%5B%22AKsRol_XfV0fHydVC5mhR_rRjOocO7ISCLSqeEABmVoDsd37DHStjgTTG40DiUEPIWJcVS8roG_LHRJBk0bcxsxOoBRbDnBE_NFOCId6OyNe_dhgzyGwD_IgxgHBSA01ladMP7BNcTVJgSWzdRQjglT-JNg_L9-G6g%3D%3D%22%5D%5D; privacy_policy_agreement=7; _im_uid.3929=b.adf1a323bfe1d6af; login_ever=yes; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=103712710=1^9=p_ab_id=2=1^10=p_ab_id_2=5=1^11=lang=zh=1; __utmb=235335808.5.10.1727058270; _ga_75BBYNYN9J=GS1.1.1727058271.2.1.1727058723.0.0.0; _ga=GA1.2.1668812789.1726887616"

    download_config.with_tag = False

    displayAllConfig()
    checkDir(download_config.store_path)

    app = UserCrawler(artist_id=random.choice(high_artist),capacity=200)
    image_ids = app.collect_urls()
    ids = []
    for id in image_ids:
        ids.append(f"https://pixiv.cat/{id}.png")
    return ids

def downloadUser():
    """
    Download artworks from a single artist

    NOTE: Require cookie for R18 images!

    Args:
        artist_id (str): artist id
        capacity (int): flow capacity, default is 1024MB
    """
    network_config.proxy["https"] = "127.0.0.1:7890"
    user_config.user_id = "user_jvey4484"
    user_config.cookie = "first_visit_datetime_pc=2024-09-21%2012%3A00%3A13; p_ab_id=2; p_ab_id_2=5; p_ab_d_id=1425353051; yuid_b=JJZmIYg; __utmc=235335808; device_token=931550d568f055adcf880fae1b9b9853; c_type=19; privacy_policy_notification=0; a_type=0; b_type=1; _im_vid=01J898CAPK2YX76S6EF910S32K; __gads=ID=c686e1054b1e97a0:T=1726887662:RT=1726887662:S=ALNI_Mah3n8iSkQm7TrRmJ2WiPhYLVtrhg; __gpi=UID=00000f12b3e37e81:T=1726887662:RT=1726887662:S=ALNI_MZ4NdsCvf3V7k4W0dx2sM4L1GNn-Q; __eoi=ID=967af6e011995033:T=1726887662:RT=1726887662:S=AA-AfjYYccT-Ev8YkpYoXBl6Mrni; __cf_bm=d0Pf.m1H07nDA_CREmcJBcNLlgmoGwpF5l2gZ25ib58-1727058269-1.0.1.1-wT1_n4TOL.sIglcM1_xxPvJvFBL5qocuo2MB3AJ0uWVIIXYmXb4SSgQlnejF7CBLdwXWggK38UY7dBDaT9Y.BRKghqAzEqLjrgIG7m4pVsA; __utma=235335808.1668812789.1726887616.1726887616.1727058270.2; __utmz=235335808.1727058270.2.2.utmcsr=bing|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; cf_clearance=fg8upL4Rklvf0juE0fz6OjJhQamRM2kfuiTT51b0nIg-1727058270-1.2.1.1-v3EfJorQo83A0hrV6zHexnI95z2VV.mS8PNrrv0YsYxVKM_NHRq85NkYTLSMJzU50Nk5E16G9ZAL_ezisjdMTncwj4skgBwRZuoFcIElFUn_lPEuvZ_.W4Mi8MR6IzUikVS7Zdc1zFjD8ZO9Xbr2CIVsniphe39lhZM6FV0kOzzKQtAV._dWu8qWk1pyl_W70lJ1g94g8yX2FvfZ8tq4jmDp51o4_VfFx_8TNOWYAxNVr48VcWtUeflpKq7zBwx4tLXYPJEAgrBaLmmdBG.1yqwDloUL80NpvFBB7.7ngtHci1nfDHKU3.ZrQ5yA3.LC9Nd6Hj_vxbLXF7wUz78JxdromdpLJXv_5S6zXScsfnU_.3cgw2B_5KtfZDchHB4Sq78_DCxS_aVuqOMfwyBfXw; _gid=GA1.2.1820646992.1727058272; PHPSESSID=103712710_UuOw0AAwB1tnYrgr55AJJ5XKgzl27bTn; _ga_MZ1NL4PHH0=GS1.1.1727058284.1.1.1727058358.0.0.0; FCNEC=%5B%5B%22AKsRol_XfV0fHydVC5mhR_rRjOocO7ISCLSqeEABmVoDsd37DHStjgTTG40DiUEPIWJcVS8roG_LHRJBk0bcxsxOoBRbDnBE_NFOCId6OyNe_dhgzyGwD_IgxgHBSA01ladMP7BNcTVJgSWzdRQjglT-JNg_L9-G6g%3D%3D%22%5D%5D; privacy_policy_agreement=7; _im_uid.3929=b.adf1a323bfe1d6af; login_ever=yes; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=103712710=1^9=p_ab_id=2=1^10=p_ab_id_2=5=1^11=lang=zh=1; __utmb=235335808.5.10.1727058270; _ga_75BBYNYN9J=GS1.1.1727058271.2.1.1727058723.0.0.0; _ga=GA1.2.1668812789.1726887616"

    download_config.with_tag = False

    displayAllConfig()
    checkDir(download_config.store_path)

    app = UserCrawler(artist_id="38297201",capacity=200)
    app.run()
def downloadKeyword(keyword):
    """
    Download search results of a keyword (sorted by popularity if order=True)
    Support advanced search, e.g. "(Lucy OR 边缘行者) AND (5000users OR 10000users)", refer to https://www.pixiv.help/hc/en-us/articles/235646387-I-would-like-to-know-how-to-search-for-content-on-pixiv

    NOTE: Require cookie for R18 images!
    NOTE: Require premium account for popularity sorting!

    Args:
        keyword (str): search keyword
        order (bool): order by popularity or not, default is False
        mode (str): content mode, default is "safe", support ["safe", "r18", "all"]
        n_images (int): max download number, default is 200
        capacity (int): flow capacity, default is 1024MB
    """
    network_config.proxy["https"] = "127.0.0.1:7890"
    user_config.user_id = "user_jvey4484"
    user_config.cookie = "first_visit_datetime_pc=2024-09-21%2012%3A00%3A13; p_ab_id=2; p_ab_id_2=5; p_ab_d_id=1425353051; yuid_b=JJZmIYg; __utmc=235335808; device_token=931550d568f055adcf880fae1b9b9853; c_type=19; privacy_policy_notification=0; a_type=0; b_type=1; _im_vid=01J898CAPK2YX76S6EF910S32K; __gads=ID=c686e1054b1e97a0:T=1726887662:RT=1726887662:S=ALNI_Mah3n8iSkQm7TrRmJ2WiPhYLVtrhg; __gpi=UID=00000f12b3e37e81:T=1726887662:RT=1726887662:S=ALNI_MZ4NdsCvf3V7k4W0dx2sM4L1GNn-Q; __eoi=ID=967af6e011995033:T=1726887662:RT=1726887662:S=AA-AfjYYccT-Ev8YkpYoXBl6Mrni; __cf_bm=d0Pf.m1H07nDA_CREmcJBcNLlgmoGwpF5l2gZ25ib58-1727058269-1.0.1.1-wT1_n4TOL.sIglcM1_xxPvJvFBL5qocuo2MB3AJ0uWVIIXYmXb4SSgQlnejF7CBLdwXWggK38UY7dBDaT9Y.BRKghqAzEqLjrgIG7m4pVsA; __utma=235335808.1668812789.1726887616.1726887616.1727058270.2; __utmz=235335808.1727058270.2.2.utmcsr=bing|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; cf_clearance=fg8upL4Rklvf0juE0fz6OjJhQamRM2kfuiTT51b0nIg-1727058270-1.2.1.1-v3EfJorQo83A0hrV6zHexnI95z2VV.mS8PNrrv0YsYxVKM_NHRq85NkYTLSMJzU50Nk5E16G9ZAL_ezisjdMTncwj4skgBwRZuoFcIElFUn_lPEuvZ_.W4Mi8MR6IzUikVS7Zdc1zFjD8ZO9Xbr2CIVsniphe39lhZM6FV0kOzzKQtAV._dWu8qWk1pyl_W70lJ1g94g8yX2FvfZ8tq4jmDp51o4_VfFx_8TNOWYAxNVr48VcWtUeflpKq7zBwx4tLXYPJEAgrBaLmmdBG.1yqwDloUL80NpvFBB7.7ngtHci1nfDHKU3.ZrQ5yA3.LC9Nd6Hj_vxbLXF7wUz78JxdromdpLJXv_5S6zXScsfnU_.3cgw2B_5KtfZDchHB4Sq78_DCxS_aVuqOMfwyBfXw; _gid=GA1.2.1820646992.1727058272; PHPSESSID=103712710_UuOw0AAwB1tnYrgr55AJJ5XKgzl27bTn; _ga_MZ1NL4PHH0=GS1.1.1727058284.1.1.1727058358.0.0.0; FCNEC=%5B%5B%22AKsRol_XfV0fHydVC5mhR_rRjOocO7ISCLSqeEABmVoDsd37DHStjgTTG40DiUEPIWJcVS8roG_LHRJBk0bcxsxOoBRbDnBE_NFOCId6OyNe_dhgzyGwD_IgxgHBSA01ladMP7BNcTVJgSWzdRQjglT-JNg_L9-G6g%3D%3D%22%5D%5D; privacy_policy_agreement=7; _im_uid.3929=b.adf1a323bfe1d6af; login_ever=yes; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=103712710=1^9=p_ab_id=2=1^10=p_ab_id_2=5=1^11=lang=zh=1; __utmb=235335808.5.10.1727058270; _ga_75BBYNYN9J=GS1.1.1727058271.2.1.1727058723.0.0.0; _ga=GA1.2.1668812789.1726887616"

    download_config.with_tag = False

    displayAllConfig()
    checkDir(download_config.store_path)

    app = KeywordCrawler(
        keyword=f"{keyword} AND (1000users OR 5000users OR 10000users)",
        order=False,
        mode=["safe", "r18", "all"][-1],
        n_images=20)
    app.run()

def downloadKeyword_urls(keyword):
    """
    Download search results of a keyword (sorted by popularity if order=True)
    Support advanced search, e.g. "(Lucy OR 边缘行者) AND (5000users OR 10000users)", refer to https://www.pixiv.help/hc/en-us/articles/235646387-I-would-like-to-know-how-to-search-for-content-on-pixiv

    NOTE: Require cookie for R18 images!
    NOTE: Require premium account for popularity sorting!

    Args:
        keyword (str): search keyword
        order (bool): order by popularity or not, default is False
        mode (str): content mode, default is "safe", support ["safe", "r18", "all"]
        n_images (int): max download number, default is 200
        capacity (int): flow capacity, default is 1024MB
    """
    network_config.proxy["https"] = "127.0.0.1:7890"
    user_config.user_id = "user_jvey4484"
    user_config.cookie = "first_visit_datetime_pc=2024-09-21%2012%3A00%3A13; p_ab_id=2; p_ab_id_2=5; p_ab_d_id=1425353051; yuid_b=JJZmIYg; __utmc=235335808; device_token=931550d568f055adcf880fae1b9b9853; c_type=19; privacy_policy_notification=0; a_type=0; b_type=1; _im_vid=01J898CAPK2YX76S6EF910S32K; __gads=ID=c686e1054b1e97a0:T=1726887662:RT=1726887662:S=ALNI_Mah3n8iSkQm7TrRmJ2WiPhYLVtrhg; __gpi=UID=00000f12b3e37e81:T=1726887662:RT=1726887662:S=ALNI_MZ4NdsCvf3V7k4W0dx2sM4L1GNn-Q; __eoi=ID=967af6e011995033:T=1726887662:RT=1726887662:S=AA-AfjYYccT-Ev8YkpYoXBl6Mrni; __cf_bm=d0Pf.m1H07nDA_CREmcJBcNLlgmoGwpF5l2gZ25ib58-1727058269-1.0.1.1-wT1_n4TOL.sIglcM1_xxPvJvFBL5qocuo2MB3AJ0uWVIIXYmXb4SSgQlnejF7CBLdwXWggK38UY7dBDaT9Y.BRKghqAzEqLjrgIG7m4pVsA; __utma=235335808.1668812789.1726887616.1726887616.1727058270.2; __utmz=235335808.1727058270.2.2.utmcsr=bing|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; cf_clearance=fg8upL4Rklvf0juE0fz6OjJhQamRM2kfuiTT51b0nIg-1727058270-1.2.1.1-v3EfJorQo83A0hrV6zHexnI95z2VV.mS8PNrrv0YsYxVKM_NHRq85NkYTLSMJzU50Nk5E16G9ZAL_ezisjdMTncwj4skgBwRZuoFcIElFUn_lPEuvZ_.W4Mi8MR6IzUikVS7Zdc1zFjD8ZO9Xbr2CIVsniphe39lhZM6FV0kOzzKQtAV._dWu8qWk1pyl_W70lJ1g94g8yX2FvfZ8tq4jmDp51o4_VfFx_8TNOWYAxNVr48VcWtUeflpKq7zBwx4tLXYPJEAgrBaLmmdBG.1yqwDloUL80NpvFBB7.7ngtHci1nfDHKU3.ZrQ5yA3.LC9Nd6Hj_vxbLXF7wUz78JxdromdpLJXv_5S6zXScsfnU_.3cgw2B_5KtfZDchHB4Sq78_DCxS_aVuqOMfwyBfXw; _gid=GA1.2.1820646992.1727058272; PHPSESSID=103712710_UuOw0AAwB1tnYrgr55AJJ5XKgzl27bTn; _ga_MZ1NL4PHH0=GS1.1.1727058284.1.1.1727058358.0.0.0; FCNEC=%5B%5B%22AKsRol_XfV0fHydVC5mhR_rRjOocO7ISCLSqeEABmVoDsd37DHStjgTTG40DiUEPIWJcVS8roG_LHRJBk0bcxsxOoBRbDnBE_NFOCId6OyNe_dhgzyGwD_IgxgHBSA01ladMP7BNcTVJgSWzdRQjglT-JNg_L9-G6g%3D%3D%22%5D%5D; privacy_policy_agreement=7; _im_uid.3929=b.adf1a323bfe1d6af; login_ever=yes; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=103712710=1^9=p_ab_id=2=1^10=p_ab_id_2=5=1^11=lang=zh=1; __utmb=235335808.5.10.1727058270; _ga_75BBYNYN9J=GS1.1.1727058271.2.1.1727058723.0.0.0; _ga=GA1.2.1668812789.1726887616"

    download_config.with_tag = False

    displayAllConfig()
    checkDir(download_config.store_path)

    app = KeywordCrawler(
        keyword=f"{keyword} AND (500users OR 1000users OR 5000users OR 10000users)",
        order=False,
        mode=["safe", "r18", "all"][0],
        n_images=20)
    image_ids = app.collect_urls()
    ids = []
    for id in image_ids:
        ids.append(f"https://pixiv.cat/{id}.png")
    return ids
def downloadKeyword_urls_r18(keyword):
    """
    Download search results of a keyword (sorted by popularity if order=True)
    Support advanced search, e.g. "(Lucy OR 边缘行者) AND (5000users OR 10000users)", refer to https://www.pixiv.help/hc/en-us/articles/235646387-I-would-like-to-know-how-to-search-for-content-on-pixiv

    NOTE: Require cookie for R18 images!
    NOTE: Require premium account for popularity sorting!

    Args:
        keyword (str): search keyword
        order (bool): order by popularity or not, default is False
        mode (str): content mode, default is "safe", support ["safe", "r18", "all"]
        n_images (int): max download number, default is 200
        capacity (int): flow capacity, default is 1024MB
    """
    network_config.proxy["https"] = "127.0.0.1:7890"
    user_config.user_id = "user_jvey4484"
    user_config.cookie = "first_visit_datetime_pc=2024-09-21%2012%3A00%3A13; p_ab_id=2; p_ab_id_2=5; p_ab_d_id=1425353051; yuid_b=JJZmIYg; __utmc=235335808; device_token=931550d568f055adcf880fae1b9b9853; c_type=19; privacy_policy_notification=0; a_type=0; b_type=1; _im_vid=01J898CAPK2YX76S6EF910S32K; __gads=ID=c686e1054b1e97a0:T=1726887662:RT=1726887662:S=ALNI_Mah3n8iSkQm7TrRmJ2WiPhYLVtrhg; __gpi=UID=00000f12b3e37e81:T=1726887662:RT=1726887662:S=ALNI_MZ4NdsCvf3V7k4W0dx2sM4L1GNn-Q; __eoi=ID=967af6e011995033:T=1726887662:RT=1726887662:S=AA-AfjYYccT-Ev8YkpYoXBl6Mrni; __cf_bm=d0Pf.m1H07nDA_CREmcJBcNLlgmoGwpF5l2gZ25ib58-1727058269-1.0.1.1-wT1_n4TOL.sIglcM1_xxPvJvFBL5qocuo2MB3AJ0uWVIIXYmXb4SSgQlnejF7CBLdwXWggK38UY7dBDaT9Y.BRKghqAzEqLjrgIG7m4pVsA; __utma=235335808.1668812789.1726887616.1726887616.1727058270.2; __utmz=235335808.1727058270.2.2.utmcsr=bing|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; cf_clearance=fg8upL4Rklvf0juE0fz6OjJhQamRM2kfuiTT51b0nIg-1727058270-1.2.1.1-v3EfJorQo83A0hrV6zHexnI95z2VV.mS8PNrrv0YsYxVKM_NHRq85NkYTLSMJzU50Nk5E16G9ZAL_ezisjdMTncwj4skgBwRZuoFcIElFUn_lPEuvZ_.W4Mi8MR6IzUikVS7Zdc1zFjD8ZO9Xbr2CIVsniphe39lhZM6FV0kOzzKQtAV._dWu8qWk1pyl_W70lJ1g94g8yX2FvfZ8tq4jmDp51o4_VfFx_8TNOWYAxNVr48VcWtUeflpKq7zBwx4tLXYPJEAgrBaLmmdBG.1yqwDloUL80NpvFBB7.7ngtHci1nfDHKU3.ZrQ5yA3.LC9Nd6Hj_vxbLXF7wUz78JxdromdpLJXv_5S6zXScsfnU_.3cgw2B_5KtfZDchHB4Sq78_DCxS_aVuqOMfwyBfXw; _gid=GA1.2.1820646992.1727058272; PHPSESSID=103712710_UuOw0AAwB1tnYrgr55AJJ5XKgzl27bTn; _ga_MZ1NL4PHH0=GS1.1.1727058284.1.1.1727058358.0.0.0; FCNEC=%5B%5B%22AKsRol_XfV0fHydVC5mhR_rRjOocO7ISCLSqeEABmVoDsd37DHStjgTTG40DiUEPIWJcVS8roG_LHRJBk0bcxsxOoBRbDnBE_NFOCId6OyNe_dhgzyGwD_IgxgHBSA01ladMP7BNcTVJgSWzdRQjglT-JNg_L9-G6g%3D%3D%22%5D%5D; privacy_policy_agreement=7; _im_uid.3929=b.adf1a323bfe1d6af; login_ever=yes; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=103712710=1^9=p_ab_id=2=1^10=p_ab_id_2=5=1^11=lang=zh=1; __utmb=235335808.5.10.1727058270; _ga_75BBYNYN9J=GS1.1.1727058271.2.1.1727058723.0.0.0; _ga=GA1.2.1668812789.1726887616"

    download_config.with_tag = False

    displayAllConfig()
    checkDir(download_config.store_path)

    app = KeywordCrawler(
        keyword=f"{keyword} AND (500users OR 1000users OR 5000users OR 10000users)",
        order=False,
        mode=["safe", "r18", "all"][1],
        n_images=20)
    image_ids = app.collect_urls()
    ids = []
    for id in image_ids:
        ids.append(f"https://pixiv.cat/{id}.png")
    return ids

if __name__ == "__main__":
    urls = downloadKeyword_urls_r18("泳装")
    print(urls)

