class Library
  attr_accessor :games

  def initialize(games)
    @games = games
  end

  def list
    games.each do |game|
      if block_given?
        puts yield game
      else
        puts game.name
      end
    end
  end
end
