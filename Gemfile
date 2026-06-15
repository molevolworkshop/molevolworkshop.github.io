source "https://rubygems.org"

# Updated to a version compatible with Ruby 4.x
gem "jekyll", "~> 4.3" 
gem "kramdown", "~> 2.4"
gem "kramdown-parser-gfm", "~> 1.1"
gem "jemoji"

# Minima 2.5+ is much more stable with modern Jekyll
gem "minima", "~> 2.5"

group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.17"
  gem "jekyll-seo-tag" # Highly recommended to replace bloat
end

# Keep your existing Windows-specific blocks
install_if -> { RUBY_PLATFORM =~ %r!mingw|mswin|java! } do
  gem "tzinfo", "~> 2.0"
  gem "tzinfo-data"
end

gem "webrick"