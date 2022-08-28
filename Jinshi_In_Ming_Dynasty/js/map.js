
function dfs(map, startyear, endyear, dep) {
    // console.log("callin")
    if (toString.apply(map) == "[object String]") {
        return map

    }
    if (toString.apply(map) == "[object Array]") {
        var newmap = []
        for (var i in map) {
            var fan = dfs(map[i], startyear, endyear, dep + 1)
            if (fan != null)           
            newmap.push(fan)
        }
        return newmap
    }
    // Set
    if (map['properties'] != null) {
        // console.log("properties")
        county_startyear = map['properties']['BEG_YR']
        county_endyear = map['properties']['END_YR']
        if (county_endyear < startyear || endyear < county_startyear)
            return null
    }
    newmap = {}
    if (map['people'] != null) {
        // console.log("people")
        newmap['people_num'] = 0
        for (var id in map['people']) {
            year = map['people'][id]['年份']
            if (startyear <= year && year <= endyear)
                newmap['people_num']++
        }
        for (var i in map)
            newmap[i] = map[i]
        return newmap
    }

    for (var i in map) {
        var fan=dfs(map[i], startyear, endyear, dep + 1)
        // if (fan==null)
        //     return{}
        if (fan != null)    
        newmap[i] = fan
        // dfs(map[i], startyear, endyear, dep + 1)
    }
    // console.log("set len", newmap.length)
    return newmap
}
//