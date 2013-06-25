<?php
// 首页
class IndexAction extends Action {
    public function index(){
 		$this->display();
// 	  $this->show('<style type="text/css">*{ padding: 0; margin: 0; } div{ padding: 4px 48px;} body{ background: #fff; font-family: "微软雅黑"; color: #333;} h1{ font-size: 100px; font-weight: normal; margin-bottom: 12px; } p{ line-height: 1.8em; font-size: 36px }</style><div style="padding: 24px 48px;"> <h1>:)</h1><p>欢迎使用 <b>ThinkPHP</b>！</p></div><script type="text/javascript" src="http://tajs.qq.com/stats?sId=9347272" charset="UTF-8"></script>','utf-8');
    }
    
    
    public function category(){
    	
    	$Model = M("aizhufu_cat");
    	$categories = $Model->order('id asc')->select();
    	foreach( $categories as $cate){
    		echo $cate['id'];
    	}
    	echo "category";
    }
    
    
    //通过编号取数据
    public function getDxBycid(){
    	//    $Model->where("id=%d and username='%s' and xx='%f'",$id,$username,$xx)->select();
    	$Model = M("aizhufu");
    	$item = $Model->where("cid=%d",$cid)->order('id asc')->select();
    	
    	echo "ops.....";
    }
    
    
}