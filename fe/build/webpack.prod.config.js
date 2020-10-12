const baseConfig = require('./webpack.base.config')
const { merge } = require('webpack-merge')

const prodConfig = merge(baseConfig, {
    mode: 'production'
})

module.exports = prodConfig