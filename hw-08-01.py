import heapq

def min_cost_cable_join(cables):
    heapq.heapify(cables)  # Створення купи зі списку кабелів
    
    total_cost = 0
    while len(cables) > 1:
        # Витягуємо два найменші кабелі та об'єднуємо їх
        min1 = heapq.heappop(cables)
        min2 = heapq.heappop(cables)
        combined_cable = min1 + min2
        total_cost += combined_cable
        
        # Додаємо об'єднаний кабель до купи
        heapq.heappush(cables, combined_cable)
    
    return total_cost

# Приклад використання
cables = [8, 5, 4, 3]
min_total_cost = min_cost_cable_join(cables)
print("Мінімальна загальна вартість з'єднання кабелів:", min_total_cost)
