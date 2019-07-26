module Jekyll
  module SortCategoryBySizeFilter
    def sort_by_size(input)
      # Sort the categories first by size (descending) and then by name
      categories = input.sort do |a, b|
        a_size = input[a[0]].size
        b_size = input[b[0]].size

        if a_size != b_size then
          b_size <=> a_size
        else
          a <=> b
        end
      end
      categories
    end
  end
end

Liquid::Template.register_filter(Jekyll::SortCategoryBySizeFilter)