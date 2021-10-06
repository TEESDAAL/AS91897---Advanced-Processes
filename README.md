# AS91897---Advanced-Processes
The repository for the AS91897 - Advanced Processes NCEA assessment (Māui's Adventure).

This is a text based game designed to be played in the terminal, while this game can be played in the python IDLE, it should be avoided.

The aim of this game is to find Te Ika-a-Māui/Aotearoa/New Zealand, before you run out of fish and starve.

You move around a grid of tiles which are shown below, using the arrow keys or WASD.

Both the Assests file and the game file are necessary.

Problems/Solutions:
  - If some characters aren't displaying properly, for example the '‾' may not display and will shows as a '?' character.
    • To solve this problem the font of the terminal should be changed to a font that supports this character, I recommend consolas as it is a monospace font
  - If the board is displayin incorrectly (this will be obvious).
    • To solve this problem the font size should be decreased, or the window size should be increased.
   

TILES:
Boat Tile:
 _______________
|    v   ~.     |
|        /|     |
|       / |     |
| v   _/__|___  |
|    \--------/ |
|~~~`~~~~~~'~~~~|
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ 
This Tile represents the player and is located at the centre of the board.
 
Te Ika-a-Māui/Aotearoa/New Zealand:
 _______________ 
|   ~    %   ~  |
| ~    ~   %% % |
|  ~   ~   %%%  |
|    ~  %%%   ~ |
| ~   %%%%  ~   |
|   %%%%  ~   ~ |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ 
Moving onto this tile wins the game.

Blank Tile:
 _______________ 
|  ~      ~     |
|      ~    ~   |
|   ~     ~     |
|      ~     ~  |
|   ~     ~     |
| ~    ~     ~  |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ 
Moving onto a blank tile has no effect.

Fish Tile:
 _______________ 
|               |
|   <><   <><   |
|     <><       |
|  <><    <><   |
|      <><      |
|               |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ 
 When the boat moves onto this tile you gain 1-3 fish, and the school of fish move to another blank tile.
 
 Storm Tile
 _______________ 
| (_ , /\  ,_/  |
|   --\ `\--`   |
|      _\ _\    |
|       `\_\    |
|       `\\     |
|         \     |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ 
 When the boat moves onto this tile you lose 1-3 fish, and the storm is blown to another blank tile.
 
 
