var app = app || {};

(function(){
    app.PlayerView = Backbone.View.extend({
        el: $('#player-container'),

        template: _.template($('#player-template').html()),

        events: {
            'click #player-close': 'closePlayer'
        },

        initialize: function(){
            _.bindAll(this, 'render', 'openPlayer', 'closePlayer', 'show', 'hide');
            this.render();
        },

        render: function(){
            $(this.el).html(this.template());
            this.iframe_container = $('div#iframe-container', this.el);
            this.player_name = $('div#player-name', this.el);
        },

        openPlayer: function(iframe, channel_model){
            this.player_name.html(channel_model.get('name'));
            this.iframe_container.html(iframe);
            $('iframe', this.el).css('width', '100%');
            $('iframe', this.el).css('height', '100%');
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