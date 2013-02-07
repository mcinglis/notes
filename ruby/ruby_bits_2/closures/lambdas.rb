
class Library
  attr_accessor :games

  def initialize(games)
    @games = games
  end

  def exec_game(name, action)
    game = games.detect { |g| g.name = name }
    action.call(game)
  end
end

library = Library.new(GAMES)
print_details = lambda do |game|
  puts "#{game.name} (#{game.system} - #{game.year})"
end
library.exec_game("Contra", print_details)

