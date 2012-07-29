Person = Backbone.Model.extend({
    defaults:{
        //默认的值
        name:'Eric',
        age:0,
        children:[]
    },
    validate:function(attributes){
      //模型的验证方法
        if( attributes.age < 0 && attributes.name == "err" ){
           return "你的年纪不能为负数或名字不能为err";
       }
    },
    initialize:function(){
       //初始化会触发
        //alert('Welcome to this world');

        this.bind('error',function(model,error){
            alert(error);
        });

        //这是绑定name属性改变时的事件，初始时不会调用，只有用定义函数调用
        this.bind('change:name',function(){
            var name = this.get('name');
            alert('changed my name to ' + name);
        });
    },
    adopt:function(newChildsName){
        //添加新方法，给数组加值,get,set
        var children_array = this.get('children');
        children_array.push(newChildsName);
        this.set('children',children_array);
    },
    replaceNameAttr:function(name){
        //定义一个改变name属性的方式
        this.set({name:name});
    }
});

SearchView = Backbone.View.extend({
    initialize: function(){
        this.render();
    },
    render: function(){
        var variables = { search_label: "My Search" };
        // Compile the template using underscore
        var template = _.template( $("#search_template").html(),variables );

        console.log(template);

        // Load the compiled HTML into the Backbone "el"
        $(this.el).html(template);
    },
    events:{
        'click input[type=button]':'doSearch'
    },
    doSearch:function(event){
        console.log(event);
        alert('search for' + $("#search_input").val());
    }
});


var Song = Backbone.Model.extend({
    defaults: {
        name: "Not specified",
        artist: "Not specified"
    },
    initialize: function(){
        console.log("Music is the answer");
    }
});

var Album = Backbone.Collection.extend({
    model: Song
});



$(function(){

  /******* Btn1 ***********/

    $('#btn1').click(function(){
        var person = new Person();
        var _txt = person.get('name')  + "  " + person.get('age') + "  " + person.get('children');
        person = new Person({name:'tommy',age:99,children:['Ryan']});
        _txt += "<br/>" + person.get('name')  + "  " + person.get('age') + "  " + person.get('children');
        person =  new Person({name:'tommy',age:99,children:['Ryan']});
        person.adopt('jason');
        _txt += "<br/>" + person.get('name')  + "  " + person.get('age') + "  " + person.get('children');
//        person.replaceNameAttr('test');

       //这两种方式一样
       var attributes =  person.toJSON();
        console.log(attributes);
        console.log(person.attributes);

        //验证
        var person = new Person;
        person.set({ name: "err1", age: -1 });
        person.set({ name: "err", age: -1 });

        $('#btn1_txt').html(_txt);
    });


    /******* Btn1 ***********/

    $('#btn2').click(function(){

        var search_view = new SearchView({ el: $("#btn2_txt") });
    });


    $('#btn3').click(function(){

        var AppRouter = Backbone.Router.extend({
            routes: {

                "/posts/:id": "getPost",
                // <a href="http://example.com/#/posts/121">Example</a>

                "/download/*path": "downloadFile",
                // <a href="http://example.com/#/download/user/images/hey.gif">Download</a>

                "/:route/:action": "loadView"
                // <a href="http://example.com/#/dashboard/graph">Load Route/Action View</a>

            },

            getPost: function( id ){
                alert(id); // 121
            },
            downloadFile: function( path ){
                alert(path); // user/images/hey.gif
            },
            loadView: function( route, action ){
                alert(route + "_" + action); // dashboard_graph
            }
        });
        // Instantiate the router
        var app_router = new AppRouter;
        // Start Backbone history a neccesary step for bookmarkable URL's
        Backbone.history.start();
    });

    $('#btn4').click(function(){
        var song1 = new Song({ name: "How Bizarre", artist: "OMC" });
        var song2 = new Song({ name: "Sexual Healing", artist: "Marvin Gaye" });
        var song3 = new Song({ name: "Talk It Over In Bed", artist: "OMC" });

        var myAlbum = new Album([ song1, song2, song3]);

        console.log(myAlbum.models);

    });

});
