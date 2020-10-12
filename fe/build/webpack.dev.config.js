const baseConfig = require('./webpack.base.config')
const { merge } = require('webpack-merge')
const path = require('path')

const devConfig = merge(baseConfig, {
    output: {
        filename: '[name].js',
        publicPath: '/static/',
        path: path.resolve(__dirname, '..', '..', 'flaskr', 'static')
    },
    mode: 'development'
})

module.exports = devConfig