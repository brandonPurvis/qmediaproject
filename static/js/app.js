var app = app || {};

$(function(){
    // Initialize Collections
    app.channelList = new app.ChannelList();
    app.filterList = new app.FilterList();

    // Initialize Components
    app.appView = new app.AppView();
    app.aboutView = new app.AboutView();
    app.aboutView.hide();


    app.playerView = new app.PlayerView();
    app.playerView.hide();

    app.menuView = new app.MenuView();

    app.channelList.fetch();
    app.filterList.fetch();
});
