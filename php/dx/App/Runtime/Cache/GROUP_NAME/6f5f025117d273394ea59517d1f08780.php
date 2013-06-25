<?php if (!defined('THINK_PATH')) exit();?><!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
<link rel="stylesheet" type="text/css" href="__PUBLIC__/Css/css/bootstrap.css" />
<style type="text/css">
body {
        padding-top: 60px;
        padding-bottom: 40px;
      }
      .sidebar-nav {
        padding: 9px 0;
      }

      @media (max-width: 980px) {
        /* Enable use of floated navbar text */
        .navbar-text.pull-right {
          float: none;
          padding-left: 5px;
          padding-right: 5px;
        }
}
</style>
<link rel="stylesheet" type="text/css" href="__PUBLIC__/Css/css/bootstrap-responsive.css" />

<script language="Javascript">
 var URL = '__URL__';
 var APP = '__APP__';
 var PUBLIC = '__PUBLIC__';
</script>
</head>
<body>
 
 <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container-fluid">
          <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="brand" href="#">Project name</a>
          <div class="nav-collapse collapse">
            <p class="navbar-text pull-right">
              Logged in as <a href="#" class="navbar-link">Username</a>
            </p>
            <ul class="nav">
              <li class="active"><a href="#">Home</a></li>
              <li><a href="/admin/about">About</a></li>
              <li><a href="#contact">Contact</a></li>
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>

    <div class="container-fluid">
      <div class="row-fluid">
        <div class="span3">
          <div class="well sidebar-nav">
            <ul class="nav nav-list">
              <li class="nav-header">数据</li>
              <li class="active"><a href="#">首页</a></li>
              <li><a href="/admin/categorylist">分类</a></li>
              <li><a href="/admin/itemlist">ITEMS</a></li>
              <li><a href="/admin/userlist">Link</a></li>
              <li class="nav-header">Sidebar</li>
              <li><a href="#">Link</a></li>
              <li><a href="#">Link</a></li>
              <li><a href="#">Link</a></li>
              <li><a href="#">Link</a></li>
              <li><a href="#">Link</a></li>
              <li><a href="#">Link</a></li>
              <li class="nav-header">管理</li>
              <li><a href="{{ url_for('admin.hakuzymovies') }}">测试</a></li>
              <li><a href="/admin/initdata">初始数据</a></li>
              <li><a href="#">Link</a></li>
            </ul>
          </div><!--/.well -->
        </div><!--/span-->
       

        <div class="span9">
          
          {% block body %}{% endblock %}

        </div><!--/span-->
      

      </div><!--/row-->

      <hr>

      <footer>
        <p>&copy; Company 2013</p>
      </footer>

    </div><!--/.fluid-container-->
 
 

<script type="text/javascript" src="__PUBLIC__/lib/jquery-1.9.1.min.js"></script>
<script type="text/javascript" src="__PUBLIC__/Css/js/bootstrap.js"></script>
</body>
</html>