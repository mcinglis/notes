
class Library
  attr_accessor :games

  def initialize(games)
    @games = games
  end

  def names
    # games.map { |game| game.name }
    games.map(&:name)
  end
end

