# N-Queens Problem with Visualisation

DAA project demonstrating **Backtracking**, **Bitmask Optimisation**, and constraint solving.

## Features
- Naive backtracking with attack checking
- Animated queen placement, conflicts, and backtracking
- First-solution mode
- Bitmask-based all-solutions counter
- Python CLI supporting N = 1 to 20 (large N may take significant time)
- Responsive web interface deployable with GitHub Pages

## Run the web visualizer
Open `index.html` in a browser, or use VS Code Live Server.

## Python solver
```bash
python nqueens.py 8
python nqueens.py 8 --all
```

## Deploy on GitHub Pages
1. Create a new GitHub repository, e.g. `N-Queens-Visualizer`.
2. Upload all files from this project and commit them.
3. Open **Settings → Pages**.
4. Under **Build and deployment**, choose **Deploy from a branch**.
5. Select `main` and `/ (root)`, then Save.
6. GitHub will provide the live Pages URL after deployment.

## Algorithm complexity
Naive backtracking has exponential search complexity. Bitmasks make column and diagonal availability checks constant-time and greatly reduce overhead.

## Possible extensions
N-Rooks, N-Knights, symmetry reduction, performance charts, and all-solution board gallery.
