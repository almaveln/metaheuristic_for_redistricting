from entities import RegionMap, District, Units


def check_if_contiguous(district: District):
    """Returns True if district is contiguous. Assumes all units are from the same district"""

    district_units = district.units
    root = next(iter(district_units))

    queue = [root]
    result = set()
    result.add(root)
    while queue:
        local_root = queue.pop(0)
        neighbors = district.get_district_neighbors_of(local_root)
        for unit in neighbors:
            if unit not in result:
                result.add(unit)
                queue.append(unit)

    # print(result)
    # print(district_units)
    return len(result) > 0 and len(result) == len(district_units)


def check_if_has_holes(sln: RegionMap):
    districts = sln.districts

    for dist in districts:
        neighboring_districts = sln.get_neighboring_districts_of(dist)
        if len(neighboring_districts) > 1:
            continue

        units_on_region_border = dist.get_district_units_on_region_border()
        if len(units_on_region_border) == 0:
            return True

    return False
