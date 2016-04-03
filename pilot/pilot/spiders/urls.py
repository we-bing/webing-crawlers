prefix = "http://info.nec.go.kr/"

city_index = prefix + "bizcommon/selectbox/selectbox_cityCodeBySgJson.json?electionId=0020160413&electionCode=2"

district_index = prefix + "bizcommon/selectbox/selectbox_getSggCityCodeJson.json?electionId=0020160413&electionCode=2&cityCode=%s"

candidacy_index = prefix + 'electioninfo/electionInfo_report.xhtml?electionId=0020160413&requestURI=%2FWEB-INF%2Fjsp%2Felectioninfo%2F0020160413%2Fcp%2Fcpri03.jsp&topMenuId=CP&secondMenuId=CPRI03&menuId=CPRI03&statementId=CPRI03_%232&electionCode=2&cityCode={0}&sggCityCode={1}&proportionalRepresentationCode=-1&townCode=-1&sggTownCode=-1'
town_index = prefix + "electioninfo/electionInfo_report.xhtml?electionId=0020160413&requestURI=%2Felectioninfo%2F0020160413%2Fbi%2Fbigi05.jsp&topMenuId=BI&secondMenuId=BIGI&menuId=BIGI05&statementId=BIGI05&electionCode=2&cityCode={0}&townCode=-1&"
candidacy_keyword_index = prefix + 'electioninfo/electionInfo_report.xhtml?electionId=0020160413&requestURI=%2FWEB-INF%2Fjsp%2Felectioninfo%2F0020160413%2Fcp%2Fcpri03.jsp&topMenuId=CP&secondMenuId=CPRI03&menuId=CPRI03&statementId=CPRI03_%232&electionCode=2&cityCode={0}&sggCityCode=-1&proportionalRepresentationCode=-1&townCode=-1&sggTownCode=-1&dateCode=0&x=37&y=10'

watch_prefix = "http://watch.peoplepower21.org"
member_private = watch_prefix + "/?mid=Member&member_seq=%s"
# member_index = watch_prefix + "/New/search.php"
# member_report = watch_prefix +"/New/cm_info.php?member_seq=%s"
# member_birth = watch_prefix +"/New/cm_info.php?member_seq=%s&info_page=cm_info_private.php"

popong_prefix = "http://ko.pokr.kr"
popong_index = popong_prefix + "/person/"
popong_person = popong_prefix + "/person/%s"



