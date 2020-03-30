const purgecss = require('@fullhuman/postcss-purgecss')({
  content: [
    './src/*.js',
    './src/components/*.js',
    './src/components/views/*.js'
  ],
  defaultExtractor: content => content.match(/[\w-/:]+(?<!:)/g) || []
})

module.exports = {
  plugins: [
    require('tailwindcss'),
    require('autoprefixer'),
    ...process.env.NODE_ENV === 'production' ? [purgecss] : []
  ]
}
