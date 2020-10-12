const baseConfig = require('./webpack.base.config')
const { merge } = require('webpack-merge')
const path = require('path')

const devConfig = merge(baseConfig, {
    mode: 'development'
})

module.exports = devConfig