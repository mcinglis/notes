
class Library
  attr_accessor :games

  def each(&block)
    games.each do |game|
      yield game
    end
  end
end

library = Library.new(GAMES)

# library.each { |game| puts "#{game.name} (#{game.system}) - #{game.year}" }

printer = lambda do |game|
  puts "#{game.name} (#{game.system} - #{game.year})"
end

library.each(&printer)

