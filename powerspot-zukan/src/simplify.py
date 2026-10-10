import json, math, sys
src, out = sys.argv[1], sys.argv[2]
g = json.load(open(src))
K = 40.0; C = math.cos(math.radians(36))
LON0, LAT0 = 128.0, 46.0
# Okinawa inset offset (in degrees, applied before projection)
OKI_DLON, OKI_DLAT = 3.6, 15.2
def proj(lon, lat, pid):
    if pid == 47:
        lon += OKI_DLON; lat += OKI_DLAT
    return ((lon-LON0)*K*C, (LAT0-lat)*K)
def dp(pts, eps):
    if len(pts) < 3: return pts
    a, b = pts[0], pts[-1]
    dmax, idx = 0, 0
    ax, ay = a; bx, by = b
    L = math.hypot(bx-ax, by-ay) or 1e-9
    for i in range(1, len(pts)-1):
        px, py = pts[i]
        d = abs((bx-ax)*(ay-py)-(ax-px)*(by-ay))/L
        if d > dmax: dmax, idx = d, i
    if dmax > eps:
        return dp(pts[:idx+1], eps)[:-1] + dp(pts[idx:], eps)
    return [a, b]
def area(r):
    s = 0
    for i in range(len(r)):
        x1,y1 = r[i]; x2,y2 = r[(i+1)%len(r)]
        s += x1*y2-x2*y1
    return abs(s)/2
res = []
for f in g['features']:
    pid = f['properties']['id']; name = f['properties']['nam_ja']
    geom = f['geometry']
    polys = geom['coordinates'] if geom['type']=='MultiPolygon' else [geom['coordinates']]
    d = []
    for poly in polys:
        ring = poly[0]
        lat = sum(p[1] for p in ring)/len(ring); lon = sum(p[0] for p in ring)/len(ring)
        if pid != 47 and lat < 29.8: continue
        if pid == 47 and lon < 127.0: continue
        pts = [proj(p[0], p[1], pid) for p in ring]
        if area(pts) < 0.6: continue
        far = max(range(len(pts)), key=lambda i: (pts[i][0]-pts[0][0])**2+(pts[i][1]-pts[0][1])**2)
        s = dp(pts[:far+1], 0.35)[:-1] + dp(pts[far:], 0.35)
        if len(s) < 4: continue
        d.append('M' + 'L'.join(f'{x:.1f},{y:.1f}' for x,y in s[:-1]) + 'Z')
    if d:
        res.append({'id': pid, 'name': name, 'd': ''.join(d)})
res.sort(key=lambda r: r['id'])
json.dump(res, open(out,'w'), ensure_ascii=False, separators=(',',':'))
xs=[];ys=[]
import re
for r in res:
    for x,y in re.findall(r'(-?[\d.]+),(-?[\d.]+)', r['d']):
        xs.append(float(x)); ys.append(float(y))
print(len(res), min(xs), max(xs), min(ys), max(ys), sum(len(r['d']) for r in res))
