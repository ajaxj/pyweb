t1 关于读写access 读写mongodb


DROP TABLE IF EXISTS `bangchubao`.`zhms_caixi`;
CREATE TABLE  `bangchubao`.`zhms_caixi` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(45) DEFAULT NULL,
  `oldcontent` text,
  `catestr` varchar(20) DEFAULT NULL,
  `cateid` int(10) unsigned DEFAULT NULL,
  `content` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=536 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `bangchubao`.`zhms_category`;
CREATE TABLE  `bangchubao`.`zhms_category` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `ename` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

 满汉全席 川菜 粤菜 湘菜 鲁菜 闽菜 徽菜 浙菜 苏菜 滇菜 鄂菜 私家小厨 东北菜 客家菜 淮扬菜 海派菜 潮州菜 素食 凉菜 烘培 甜品点心 山珍 火锅 海鲜 美食DIY 汤类大全
http://www.zhms.cn/Ms_menu/xiang/2013-7/201373152737.htm
http://www.zhms.cn/Ms_menu/yue/2006-4-19/20064191913028517.htm

http://www.zhms.cn/Ms_menu/beijing/ 京菜
http://www.zhms.cn/Ms_menu/beijing/list_16.htm

http://www.zhms.cn/Ms_menu/shandong/ 鲁菜
http://www.zhms.cn/Ms_menu/shandong/list_25.htm

http://www.zhms.cn/Ms_menu/min/ 闽菜
http://www.zhms.cn/Ms_menu/min/list_14.htm


http://www.zhms.cn/Ms_menu/hui/  徽菜
http://www.zhms.cn/Ms_menu/hui/list_11.htm

http://www.zhms.cn/Ms_menu/zhe/ 浙菜
http://www.zhms.cn/Ms_menu/zhe/list_26.htm


http://www.zhms.cn/Ms_menu/shu/ 苏菜
http://www.zhms.cn/Ms_menu/shu/list_17.htm

http://www.zhms.cn/Ms_menu/ecai/ 鄂菜
http://www.zhms.cn/Ms_menu/ecai/list_5.htm

http://www.zhms.cn/Ms_menu/dian/ 滇菜
http://www.zhms.cn/Ms_menu/dian/list_7.htm

http://www.zhms.cn/Ms_menu/liao/ 辽菜
http://www.zhms.cn/Ms_menu/liao/list_2.htm

http://www.zhms.cn/Ms_menu/sjxc/ 私房
http://www.zhms.cn/Ms_menu/sjxc/list_130.htm




