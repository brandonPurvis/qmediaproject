var app = app || {};

(function(){
    app.PlayerView = Backbone.View.extend({
        el: $('#player-container'),

        template: _.template($('#player-template').html()),

        events: {
            'click #player-close': 'closePlayer'
        },

        initialize: function(){
            this.model = new app.Channel({'name': 'testing!'});
            _.bindAll(this, 'render', 'openPlayer', 'closePlayer', 'setChannelModel', 'show', 'hide');
            this.render();
        },

        render: function(){
            $(this.el).html(this.template(this.model.attributes));
        },

        setChannelModel: function(channel_model){
            this.model = channel_model;
            this.model.bind('change', this.render, this);
            this.model.setPlaylist();
            this.render();
        },


        openPlayer: function(iframe, channel_model){
            this.setChannelModel(channel_model);
            this.show();
        },

        closePlayer: function(){
            this.iframe_container.html('');
            this.hide();
        },

        show: function(){
            $(this.el).show();
        },

        hide: function(){
            $(this.el).hide();
        }
    });
})();