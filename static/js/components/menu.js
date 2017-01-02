var app = app || {};

(function(){
    app.MenuView = Backbone.View.extend({
        el: $('#menu-container'),

        template: _.template($('#menu-template').html()),

        events: {
            'click li#home-nav': 'goToHome',
            'click li#about-nav': 'goToAbout',
            'click li#random-nav': 'openRandomVideo'
        },

        initialize: function(){
            _.bindAll(this, 'render');
            this.render();
        },

        render: function(){
            $(this.el).html( this.template() );
        },

        hideAll: function(){
            app.appView.hide();
            app.aboutView.hide();
        },

        goToHome: function(){
            this.hideAll();
            app.appView.show();
        },

        goToAbout: function(){
            this.hideAll();
            app.aboutView.show();
        },

        openRandomVideo: function(){
            this.hideAll();
            app.appView.show(); // Show main app view
            $.get('/random/playlist/', '', function(resp){
                console.log("pl: " + resp);
                var placeholder_channel = new app.Channel({'name':'Random Channel'});
                console.log("phc: " + placeholder_channel);
                app.playerView.openPlayer(resp, placeholder_channel);
                app.playerView.show();
            });
        }
    });
})();