
class Library
  attr_accessor :games

  def initialize(games)
    @games = games
  end

  def exec_game(name, action, error)
    game = games.detect { |g| g.name = name }
    begin
      action.call game
    rescue
      error.call
    end
  end
end

library = Library.new(GAMES)

print_details = lambda do |game|
  puts "#{game.name} (#{game.system} - #{game.year})"
end

error_handler = lambda do
  puts "There was an error!"
end

library.exec_game("Contra", print_details, error_handler)

