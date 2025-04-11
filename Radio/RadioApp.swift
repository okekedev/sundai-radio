//
//  RadioApp.swift
//  Radio
//
//  Created by Christian Okeke on 4/10/25.
//

import SwiftUI

@main
struct RadioApp: App {
    let persistenceController = PersistenceController.shared

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(\.managedObjectContext, persistenceController.container.viewContext)
        }
    }
}
