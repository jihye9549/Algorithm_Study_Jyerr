
function dfs(start) {
  if (start >= n || start <= 0) return false;
  if (!visited[start]) {
    visited[start] = true;
    dfs(start + Arr[start]);
    dfs(start - Arr[start]);
  }
  return true;
}

dfs(start);