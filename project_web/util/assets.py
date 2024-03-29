from flask_assets import Bundle


bundles = {
    
    'home_js': Bundle(
        'js/vendor/bootstrap-4.1.3.js',
        'js/vendor/bootstrap.min.js',
        'js/vendor/google_map.js',
        # 'js/vendor/jquery-3.3.1.js',
        'js/vendor/jquery.countTo.js',
        'js/vendor/jquery.easing.1.3.js',
        'js/vendor/jquery.magnific-popup.min.js',
        'js/vendor/jquery.mb.YTPlayer.min.js',
        'js/vendor/jquery.min.js',
        'js/vendor/jquery.stellar.min.js',
        'js/vendor/jquery.waypoints.min.js',
        'js/vendor/magnific-popup-options.js',
        'js/vendor/main.js',
        'js/vendor/modernizr-2.6.2.min.js',
        'js/vendor/owl.carousel.min.js',
        'js/vendor/popper.js',
        'js/vendor/respond.min.js',
        'js/custom.js',
        filters='jsmin',
        output='gen/home.%(version)s.js'),

    'home_css': Bundle(
        'css/vendor/animate.css',
        'css/vendor/bootstrap-4.1.3.css',
        'css/vendor/bootstrap.css',
        'css/vendor/bootstrap.css.map',
        'css/vendor/flexslider.css',
        'css/vendor/icomoon.css',
        'css/vendor/magnific-popup.css',
        'css/vendor/main.css',
        'css/vendor/owl.carousel.min.css',
        # 'css/vendor/owl.theme.default.min.css',
        'css/vendor/style.css',
        'css/vendor/style.css.map',
        'css/vendor/util.css',
        'css/custom.scss',
        'sass/_bootstrap-compass.scss',
        'sass/_bootstrap-mincer.scss',
        'sass/_bootstrap-sprockets.scss',
        'sass/bootstrap.scss',
        'sass/style.scss',
        filters='cssmin',
        # filters="libsass",
        # depends=['css/*.scss'],
        output='gen/home.%(version)s.css') } 