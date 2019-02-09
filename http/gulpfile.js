var gulp = require('gulp'),
    sass = require('gulp-sass'),
    // <HTML> templating
    // fileinclude = require('gulp-file-include'),
    rename = require('gulp-rename'),
    autoprefixer = require('gulp-autoprefixer'),
    cleanCSS = require('gulp-clean-css'),
    sourcemaps = require('gulp-sourcemaps'),
    path = require("path");

var browserSync = require('browser-sync').create();

var paths = {
  sass: 'css/sass/',
  css: 'css/',
  dist: 'dist/'
};

//  Sass: compile sass to css task - uses Libsass
//===========================================
gulp.task('sass', function() {
  return gulp.src(path.join(paths.sass, '*.scss'), {base: paths.sass})
    .pipe(sass({ style: 'expanded', sourceComments: 'map', errLogToConsole: true}))
    .pipe(autoprefixer('last 2 version', "> 1%", 'ie 8', 'ie 9'))
    .pipe(gulp.dest(paths.css));
});

gulp.task('minify-css', function() {
    return gulp.src(path.join(paths.css, '*.css'))
    .pipe(sourcemaps.init())
    .pipe(cleanCSS())
    .pipe(sourcemaps.write())
    .pipe(rename(function (path) {
        path.basename += ".min";
    }))
    .pipe(gulp.dest(paths.dist))
    .pipe(browserSync.stream({match: '**/*.css'}));
});

//  Connect: sever task
//===========================================
gulp.task('server', function() {
    browserSync.init({
        server: "./"
    });
    gulp.watch('css/sass/*.scss', gulp.series('sass'));
    gulp.watch('css/*.css', gulp.series('minify-css'));
    gulp.watch('**/*.html').on('change', browserSync.reload);
});


//  Default Gulp Task
//===========================================
gulp.task('default', gulp.series('sass', 'minify-css', 'server'), function() {

});