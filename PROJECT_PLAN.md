# Simplified Village Simulation - Project Plan

## 1. Project Overview
A chill, top-down village simulation where the player controls a farmer. The world is grid-based for environmental interactions (planting, building), but the player character moves freely across the map. The goal is to create a relaxing environment with deep systems for farming, carpentry, and animal husbandry.

## 2. Core Mechanics
- **Free Movement:** The farmer moves smoothly (pixel-based) rather than jumping from tile to tile.
- **Tile-Based Interaction:** Planting crops, placing furniture, and building structures align with a 32x32 or 16x16 grid.
- **Dynamic Systems:**
    - **Farming:** Soil preparation, seeding, watering, and harvesting.
    - **Carpentry:** Using workbenches to craft furniture and tools from gathered resources.
    - **Animal Farming:** Raising livestock in pens.
    - **Interiors:** Entering buildings (houses) with separate map layouts.

## 3. Architecture
- **Language/Framework:** Python + Pygame (chosen for its simplicity and great learning curve).
- **Game Loop:** Standard `Process Input -> Update -> Render` cycle.
- **Entity System:** 
    - `Entity` base class for everything that moves or updates.
    - `Farmer` class inheriting from Entity.
    - `TileMap` class to handle the grid, collision, and rendering.
- **Coordinate Systems:**
    - **World Coordinates:** Pixel-based (for movement and rendering).
    - **Grid Coordinates:** Integer-based (for planting and building).
- **State Management:** A simple state machine to handle menus, world exploration, and indoor transitions.

## 4. Development Phases

### Phase 1: Foundation (The "Walking Simulator") [IN PROGRESS]
- [>] Initialize window and basic game loop. (Working on skeleton)
- [ ] Implement free movement for the farmer.
- [ ] Basic sprite animation (Idle/Walk).
- [ ] Setup Camera system to follow the player.

### Phase 2: The Grid & Farming
- [ ] Implement a TileMap system.
- [ ] Tile selection logic (highlighting the tile the farmer is facing).
- [ ] Basic farming cycle: Till soil -> Plant seed -> Growth stages -> Harvest.
- [ ] Simple UI for current tool/seed selection.

### Phase 3: Inventory & Items
- [ ] Item data structure (Seeds, Tools, Harvested Goods).
- [ ] Inventory system (Backpack).
- [ ] Dropping/picking up items.

### Phase 4: Structures & Interiors
- [ ] Building placement system.
- [ ] Transition logic (Going inside the house).
- [ ] Interior TileMaps.

### Phase 5: Advanced Crafting (Carpentry)
- [ ] Resource gathering (Chopping trees/Mining).
- [ ] Workbench interaction.
- [ ] Crafting recipes and furniture placement.

### Phase 6: Animals & Life
- [ ] Basic AI for animals (wandering, eating).
- [ ] Fencing and animal pens.
- [ ] Time/Day cycle.

### Phase 7: Infrastructure & Polish
- [ ] Save/Load system (JSON or SQLite).
- [ ] Sound effects and background music.
- [ ] CI/CD pipeline (GitHub Actions) for automated testing and linting.

## 5. Technical Decisions
- **Rendering:** Layered rendering (Background -> Tiles -> Entities -> UI).
- **Collision:** Simple AABB (Axis-Aligned Bounding Box) for static obstacles.
- **Data Management:** Use external JSON files for item definitions and crafting recipes to allow easy modification.
