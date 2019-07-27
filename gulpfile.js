var gulp = require('gulp'),
    autoprefixer = require('gulp-autoprefixer'),
    rename = require('gulp-rename'),
    packageFile = require('./package.json');
    sass = require('gulp-sass'),

gulp.task('styles', function () {
    return gulp.src('assets/scss/bundle.scss', { base: '.' })
        .pipe(sass({
            precision: 8,
            outputStyle: 'expanded'
        }).on('error', sass.logError))
        .pipe(autoprefixer({
            browsers: packageFile.browserslist,
            cascade: false
        }))
        .pipe(rename('dashboard.css'))
        .pipe(gulp.dest('assets/css/'));
});

gulp.task('styles-plugins', function () {
    return gulp.src('assets/plugins/**/plugin.scss', { base: '.' })
        .pipe(sass({
            precision: 6,
            outputStyle: 'expanded'
        }).on('error', sass.logError))
        .pipe(autoprefixer({
            browsers: packageFile.browserslist,
            cascade: false
        }))
        .pipe(rename(function(path) {
            path.extname = '.css';
        }))
        .pipe(gulp.dest('.'));
});

gulp.task('watch', ['styles', 'styles-plugins'], function() {
    gulp.watch('assets/scss/**/*.scss', ['styles']);
    gulp.watch('assets/plugins/**/*.scss', ['styles-plugins']);
});

gulp.task('build', ['styles', 'styles-plugins']);