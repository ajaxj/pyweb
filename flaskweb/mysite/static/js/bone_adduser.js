$(function(){

    Friend = Backbone.Model.extend({
        defaults:{
            name:null
        }
    });

    Friends = Backbone.Collection.extend({
        url:'/savefriend',
        model:Friend,
        initialize:function(options){
            //使用传递视图，调用视图里的方式
            this.bind('add',options.view.addFriendLi);
            //自定义的方法
            this.bind('add',this.printcut);

            //别一种自定义的方法
            this.bind('add',function(mo1){

                 $("#friends-list2").append("<li>" + mo1.get('name') + "</li>");
            });
        },
        printcut:function(mo){
            $("#friends-list").append("<li>" + mo.get('name') + "</li>");
        }
    });

    window.AppView = Backbone.View.extend({
        el:$('body'),
        initialize:function(){
          this.friends = new Friends({view:this});
        },
        events:{
            'click #add-friend':'showPrompt'
        },
        showPrompt:function(){
            var friend_name = prompt('你的朋友是?');
            var friend_model = new Friend({name:friend_name});
            //this.friends.add(friend_model);
            //console.log(JSON.stringify(friend_model));
            o = this.friends.create(friend_model);
            console.log(o);
            console.log(o.attributes.name + "  " + o.attributes['success']);
//            console.log(o.get('name') + " "+ success);

        },
        addFriendLi:function(model){
            $("#friends-list3").append("<li>" + model.get('name') + "</li>");
        }
    });


    var app = new AppView

});