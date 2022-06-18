class Solution:
    # Time: O(nlogn), Space: O(1) 
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        box_types, truck_size, units = boxTypes, truckSize, 0
        box_types.sort(key=lambda x: -x[1])
        for box in box_types:
            num_boxes, units_per_box = box[0], box[1]
            if truck_size - num_boxes < 0:
                num_boxes = truck_size
            truck_size -= num_boxes
            units += (num_boxes * units_per_box)
            if truck_size == 0:
                break
        return units
            
                
        
        
        