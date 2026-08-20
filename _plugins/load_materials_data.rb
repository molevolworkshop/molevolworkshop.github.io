require 'csv'
require 'yaml'
require 'json'

module Jekyll
  class MaterialsDataInjector < Generator
    safe true
    priority :high

    def generate(site)
      materials_data_dir = File.join(site.source, 'materials', '_data')
      
      # Initialize site.data['materials'] hash in memory
      site.data['materials'] = {}

      return unless Dir.exist?(materials_data_dir)

      Dir.entries(materials_data_dir).each do |entry|
        next if entry.start_with?('.')
        file_path = File.join(materials_data_dir, entry)
        next unless File.file?(file_path)

        ext = File.extname(entry).downcase
        base_name = File.basename(entry, ext)

        if ext == '.csv'
          data = []
          CSV.foreach(file_path, headers: true) do |row|
            data << row.to_h
          end
          site.data['materials'][base_name] = data
        elsif ['.yml', '.yaml'].include?(ext)
          site.data['materials'][base_name] = SafeYAML.load_file(file_path)
        elsif ext == '.json'
          site.data['materials'][base_name] = JSON.parse(File.read(file_path))
        end
      end
    end
  end
end